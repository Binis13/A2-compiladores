# -*- coding: utf-8 -*-
"""
Intérprete: executa a AST diretamente.
"""
from typing import List, Dict, Any
from .ast_nodes import *


class RuntimeErrorLang(Exception):
    pass


def exec_program(node: Program, *, trace: bool = False) -> Dict[str, Any]:
    """Executa o programa (AST) e retorna o ambiente global."""
    frames: List[Dict[str, Any]] = [{}]

    def push():
        frames.append({})
        if trace:
            print(">> push {}")

    def pop():
        frames.pop()
        if trace:
            print("<< pop {}")

    def declare(name: str, value: Any):
        frames[-1][name] = value

    def get(name: str):
        for d in reversed(frames):
            if name in d:
                return d[name]
        raise RuntimeErrorLang(f"Variável não encontrada: {name}")

    def setvar(name: str, value: Any):
        for d in reversed(frames):
            if name in d:
                d[name] = value
                return value
        frames[-1][name] = value
        return value

    def eval_expr(e):
        if isinstance(e, Num):
            return e.value
        if isinstance(e, Bool):
            return e.value
        if isinstance(e, Id):
            return get(e.name)
        if isinstance(e, NewArray):
            n = eval_expr(e.size)
            if n < 0:
                raise RuntimeErrorLang("Tamanho de array negativo.")
            base_zero = 0 if e.base == "int" else False
            return [base_zero for _ in range(int(n))]
        if isinstance(e, ArrayRef):
            arr = get(e.id.name)
            idx = eval_expr(e.index)
            if not isinstance(arr, list):
                raise RuntimeErrorLang(f"'{e.id.name}' não é array em tempo de execução.")
            if idx < 0 or idx >= len(arr):
                raise RuntimeErrorLang(f"Índice fora dos limites: {idx}")
            return arr[int(idx)]
        if isinstance(e, Unary):
            v = eval_expr(e.expr)
            if e.op == "!":
                return not bool(v)
            if e.op == "-":
                return -int(v)
            raise RuntimeErrorLang(f"Unário desconhecido: {e.op}")
        if isinstance(e, Ari):
            a = eval_expr(e.left)
            b = eval_expr(e.right)
            if e.op == "+":
                return int(a) + int(b)
            if e.op == "-":
                return int(a) - int(b)
            if e.op == "*":
                return int(a) * int(b)
            if e.op == "/":
                return int(a) // int(b)
            raise RuntimeErrorLang(f"Aritmético desconhecido: {e.op}")
        if isinstance(e, Rel):
            a = eval_expr(e.left)
            b = eval_expr(e.right)
            if e.op == "<":
                return int(a) < int(b)
            if e.op == "<=":
                return int(a) <= int(b)
            raise RuntimeErrorLang(f"Relacional desconhecido: {e.op}")
        if isinstance(e, Eq):
            a = eval_expr(e.left)
            b = eval_expr(e.right)
            if e.op == "==":
                return a == b
            if e.op == "!=":
                return a != b
            raise RuntimeErrorLang(f"Eq desconhecido: {e.op}")
        if isinstance(e, Lg):
            if e.op == "||":
                left = bool(eval_expr(e.left))
                if left:
                    return True
                return bool(eval_expr(e.right))
            if e.op == "&&":
                left = bool(eval_expr(e.left))
                if not left:
                    return False
                return bool(eval_expr(e.right))
            raise RuntimeErrorLang(f"Lógico desconhecido: {e.op}")
        if isinstance(e, Assign):
            val = eval_expr(e.right)
            if isinstance(e.left, Id):
                return setvar(e.left.name, val)
            elif isinstance(e.left, ArrayRef):
                arr = get(e.left.id.name)
                idx = eval_expr(e.left.index)
                if not isinstance(arr, list):
                    raise RuntimeErrorLang(f"'{e.left.id.name}' não é array em tempo de execução.")
                if idx < 0 or idx >= len(arr):
                    raise RuntimeErrorLang(f"Índice fora dos limites: {idx}")
                arr[int(idx)] = val
                return val
            else:
                raise RuntimeErrorLang("Atribuição inválida (lhs).")
        raise RuntimeErrorLang(f"Expressão não suportada: {type(e).__name__}")

    def exec_stmt(s):
        if isinstance(s, Block):
            push()
            exec_stmts(s.stmts)
            pop()
            return
        if isinstance(s, list):
            for stmt in s:
                exec_stmt(stmt)
            return
        if isinstance(s, Decl):
            if s.is_array:
                default = None
            else:
                default = 0 if s.typ == "int" else False
            declare(s.id.name, default)
            if s.init is not None:
                v = eval_expr(s.init)
                setvar(s.id.name, v)
            return
        if isinstance(s, Eval):
            val = eval_expr(s.expr)
            if trace:
                print(f"eval => {val}")
            return
        if isinstance(s, Print):
            vals = [eval_expr(a) for a in s.args]
            # Converte booleanos para 0/1 para saída
            vals = [1 if v is True else (0 if v is False else v) for v in vals]
            print(*vals)
            if trace:
                print(f"(printed {vals})")
            return
        if isinstance(s, If):
            cond = bool(eval_expr(s.cond))
            if trace:
                print(f"if ({cond}) ...")
            if cond:
                exec_stmt(s.then_stmt)
            elif s.else_stmt is not None:
                exec_stmt(s.else_stmt)
            return
        if isinstance(s, While):
            while True:
                cond = bool(eval_expr(s.cond))
                if trace:
                    print(f"while ({cond}) ...")
                if not cond:
                    break
                exec_stmt(s.body)
            return
        if isinstance(s, Do):
            while True:
                if trace:
                    print("do { ... }")
                exec_stmt(s.body)
                cond = bool(eval_expr(s.cond))
                if trace:
                    print(f"while ({cond});")
                if not cond:
                    break
            return
        raise RuntimeErrorLang(f"Stmt não suportado: {type(s).__name__}")

    def exec_stmts(node):
        if node is None:
            return
        if isinstance(node, list):
            for stmt in node:
                exec_stmt(stmt)
        else:
            exec_stmt(node)

    if trace:
        print(">> start Program")
    exec_stmt(node.block)
    if trace:
        print(">> end Program")
    return frames[0]
