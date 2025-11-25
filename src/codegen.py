# -*- coding: utf-8 -*-
"""
Gerador de Código: converte AST para código Python.
"""
from typing import Dict, Any, Optional
from .ast_nodes import *


def codegen_python(prog: Program) -> str:
    """Gera código Python a partir da AST."""
    out = []
    out.append("def __ml_run(env=None):")
    out.append("    frames = [env if isinstance(env, dict) else {}]")
    out.append("    def push(): frames.append({})")
    out.append("    def pop(): frames.pop()")
    out.append("    def declare(name, val): frames[-1][name] = val")
    out.append("    def get(name):")
    out.append("        for d in reversed(frames):")
    out.append("            if name in d: return d[name]")
    out.append("        raise NameError(f'Variável não encontrada: {name}')")
    out.append("    def setvar(name, val):")
    out.append("        for d in reversed(frames):")
    out.append("            if name in d: d[name]=val; return val")
    out.append("        frames[-1][name]=val; return val")
    out.extend(_cg_stmt(prog.block, indent="    "))
    out.append("    return frames[0]")
    return "\n".join(out)


def _cg_stmt(node, indent=""):
    out = []

    def emit(line):
        out.append(f"{indent}{line}")

    if isinstance(node, Block):
        emit("push()")
        out.extend(_cg_stmts(node.stmts, indent))
        emit("pop()")
        return out
    if isinstance(node, list):
        out.extend(_cg_stmts(node, indent))
        return out
    if isinstance(node, Decl):
        default = "None" if node.is_array else ("0" if node.typ == "int" else "False")
        emit(f"declare('{node.id.name}', {default})")
        if node.init is not None:
            emit(f"setvar('{node.id.name}', {_cg_expr(node.init)})")
        return out
    if isinstance(node, Eval):
        emit(f"{_cg_expr(node.expr)}  # eval")
        return out
    if isinstance(node, Print):
        # Converte cada argumento, convertendo booleanos para 0/1
        args_code = []
        for a in node.args:
            arg_expr = _cg_expr(a)
            # Wrapper para converter True/False para 1/0
            args_code.append(f"(1 if ({arg_expr}) == True else (0 if ({arg_expr}) == False else ({arg_expr})))")
        args = ", ".join(args_code)
        emit(f"print({args})")
        return out
    if isinstance(node, If):
        emit(f"if bool({_cg_expr(node.cond)}):")
        out.extend(_cg_stmt(node.then_stmt, indent + "    "))
        if node.else_stmt is not None:
            emit("else:")
            out.extend(_cg_stmt(node.else_stmt, indent + "    "))
        return out
    if isinstance(node, While):
        emit(f"while bool({_cg_expr(node.cond)}):")
        out.extend(_cg_stmt(node.body, indent + "    "))
        return out
    if isinstance(node, Do):
        emit("while True:")
        out.extend(_cg_stmt(node.body, indent + "    "))
        emit(f"    if not bool({_cg_expr(node.cond)}):")
        emit("        break")
        return out
    if isinstance(node, Assign):
        if isinstance(node.left, Id):
            emit(f"setvar('{node.left.name}', {_cg_expr(node.right)})")
        else:
            name = node.left.id.name
            idx = _cg_expr(node.left.index)
            val = _cg_expr(node.right)
            emit(f"__arr = get('{name}')")
            emit(f"__idx = int({idx})")
            emit(f"__n = len(__arr)")
            emit(f"assert 0 <= __idx < __n, 'Índice fora dos limites: %r' % (__idx,)")
            emit(f"__arr[__idx] = {val}")
        return out
    raise RuntimeError(f"Stmt desconhecido no codegen: {type(node).__name__}")


def _cg_stmts(node, indent=""):
    out = []
    if node is None:
        return out
    if isinstance(node, list):
        for stmt in node:
            out.extend(_cg_stmt(stmt, indent))
        return out
    out.extend(_cg_stmt(node, indent))
    return out


def _cg_expr(node):
    if isinstance(node, Num):
        return str(node.value)
    if isinstance(node, Bool):
        return ("True" if node.value else "False")
    if isinstance(node, Id):
        return f"get('{node.name}')"
    if isinstance(node, NewArray):
        zero = "0" if node.base == "int" else "False"
        return f"([{zero}] * int({_cg_expr(node.size)}))"
    if isinstance(node, ArrayRef):
        return f"get('{node.id.name}')[int({_cg_expr(node.index)})]"
    if isinstance(node, Unary):
        if node.op == "!":
            return f"(not bool({_cg_expr(node.expr)}))"
        if node.op == "-":
            return f"(-({_cg_expr(node.expr)}))"
        raise RuntimeError("unário desconhecido")
    if isinstance(node, Ari):
        op = "//" if node.op == "/" else node.op
        return f"({_cg_expr(node.left)} {op} {_cg_expr(node.right)})"
    if isinstance(node, Rel):
        op = "<=" if node.op == "<=" else node.op
        return f"({_cg_expr(node.left)} {op} {_cg_expr(node.right)})"
    if isinstance(node, Eq):
        return f"({_cg_expr(node.left)} {node.op} {_cg_expr(node.right)})"
    if isinstance(node, Lg):
        if node.op == "||":
            return f"(bool({_cg_expr(node.left)}) or bool({_cg_expr(node.right)}))"
        if node.op == "&&":
            return f"(bool({_cg_expr(node.left)}) and bool({_cg_expr(node.right)}))"
        raise RuntimeError("lógico desconhecido")
    if isinstance(node, Assign):
        if isinstance(node.left, Id):
            return f"setvar('{node.left.name}', {_cg_expr(node.right)})"
        else:
            name = node.left.id.name
            idx = _cg_expr(node.left.index)
            val = _cg_expr(node.right)
            return (
                f"(lambda __arr, __idx, __val: "
                f"[__arr.__setitem__(__idx, __val), __val][1])"
                f"(get('{name}'), int({idx}), {val})"
            )
    raise RuntimeError(f"Expr desconhecida no codegen: {type(node).__name__}")


def exec_generated_python(pycode: str, env: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Executa código Python gerado."""
    ns: Dict[str, Any] = {}
    exec(pycode, ns, ns)
    return ns["__ml_run"](env if env is not None else {})
