# -*- coding: utf-8 -*-
"""
Impressão em ASCII da Árvore Sintática Abstrata (AST).
"""
from dataclasses import is_dataclass
from .ast_nodes import *


def _children_of(node):
    """Retorna os filhos de um nó AST."""
    if node is None or not is_dataclass(node):
        return []
    if isinstance(node, Program):
        return [("block", node.block)]
    if isinstance(node, Block):
        if node.stmts is None:
            return [("stmts", None)]
        if isinstance(node.stmts, list):
            return [(f"stmt[{i}]", s) for i, s in enumerate(node.stmts)]
        return [("stmts", node.stmts)]
    if isinstance(node, Decl):
        return [
            ("type", Id(f"{node.typ}{'[]' if node.is_array else ''}{' const' if node.is_const else ''}")),
            ("id", node.id),
            ("init", node.init)
        ]
    if isinstance(node, Eval):
        return [("expr", node.expr)]
    if isinstance(node, Print):
        return [(f"arg[{i}]", a) for i, a in enumerate(node.args)]
    if isinstance(node, If):
        kids = [("cond", node.cond), ("then", node.then_stmt)]
        if node.else_stmt is not None:
            kids.append(("else", node.else_stmt))
        return kids
    if isinstance(node, While):
        return [("cond", node.cond), ("body", node.body)]
    if isinstance(node, Do):
        return [("body", node.body), ("cond", node.cond)]
    if isinstance(node, Assign):
        return [("left", node.left), ("right", node.right)]
    if isinstance(node, Rel):
        return [(f"left op='{node.op}'", node.left), ("right", node.right)]
    if isinstance(node, Eq):
        return [(f"left op='{node.op}'", node.left), ("right", node.right)]
    if isinstance(node, Lg):
        return [(f"left op='{node.op}'", node.left), ("right", node.right)]
    if isinstance(node, Unary):
        return [(f"op='{node.op}'", node.expr)]
    if isinstance(node, Ari):
        return [(f"left op='{node.op}'", node.left), ("right", node.right)]
    if isinstance(node, NewArray):
        return [("base", Id(node.base)), ("size", node.size)]
    if isinstance(node, ArrayRef):
        return [("id", node.id), ("index", node.index)]
    if isinstance(node, Num):
        return []
    if isinstance(node, Bool):
        return []
    if isinstance(node, Id):
        return []
    return []


def _label_of(node):
    """Retorna o rótulo de um nó AST."""
    if isinstance(node, Program):
        return "Program"
    if isinstance(node, Block):
        return "Block"
    if isinstance(node, Decl):
        return f"Decl({node.typ}{'[]' if node.is_array else ''}{', const' if node.is_const else ''})"
    if isinstance(node, Eval):
        return "Eval"
    if isinstance(node, Print):
        return "Print"
    if isinstance(node, If):
        return "If"
    if isinstance(node, While):
        return "While"
    if isinstance(node, Do):
        return "Do"
    if isinstance(node, Assign):
        return "Assign"
    if isinstance(node, Rel):
        return f"Rel(op='{node.op}')"
    if isinstance(node, Eq):
        return f"Eq(op='{node.op}')"
    if isinstance(node, Lg):
        return f"Lg(op='{node.op}')"
    if isinstance(node, Unary):
        return f"Unary(op='{node.op}')"
    if isinstance(node, Ari):
        return f"Ari(op='{node.op}')"
    if isinstance(node, NewArray):
        return "NewArray"
    if isinstance(node, ArrayRef):
        return "ArrayRef"
    if isinstance(node, Num):
        return f"Num({node.value})"
    if isinstance(node, Bool):
        return f"Bool({node.value})"
    if isinstance(node, Id):
        return f"Id({node.name})"
    return type(node).__name__


def print_ast_ascii(node, *, show_edge_labels=True):
    """Imprime a AST em formato ASCII."""
    def rec(n, prefix="", is_last=True, edge_label=None):
        # Usar apenas caracteres ASCII
        connector = "`-- " if is_last else "|-- "
        if edge_label and show_edge_labels:
            line = f"{prefix}{connector}[{edge_label}] {_label_of(n)}"
        else:
            line = f"{prefix}{connector}{_label_of(n)}"
        print(line)
        new_prefix = f"{prefix}    " if is_last else f"{prefix}|   "
        kids = _children_of(n)
        for i, (elabel, child) in enumerate(kids):
            last = (i == len(kids) - 1)
            if child is None:
                none_line = f"{new_prefix}{'`-- ' if last else '|-- '}"
                none_line += f"[{elabel}] None" if show_edge_labels else "None"
                print(none_line)
            else:
                rec(child, new_prefix, last, elabel)

    print(_label_of(node))
    kids = _children_of(node)
    for i, (elabel, child) in enumerate(kids):
        last = (i == len(kids) - 1)
        if child is None:
            print(f"{'`-- ' if last else '|-- '}[{elabel}] None")
        else:
            rec(child, "", last, elabel)
