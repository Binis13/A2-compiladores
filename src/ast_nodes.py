# -*- coding: utf-8 -*-
"""
Classes para representar a Árvore Sintática Abstrata (AST) da MiniLang.
"""
from dataclasses import dataclass, is_dataclass
from typing import Optional, List, Any


# =========================================================
# AST Node Classes
# =========================================================

@dataclass
class Program:
    block: "Block"


@dataclass
class Block:
    stmts: Optional[object]  # List[stmt] ou None


@dataclass
class Decl:
    typ: str               # "int" | "bool"
    is_array: bool
    is_const: bool
    id: "Id"
    init: Optional[object] = None  # expr ou NewArray


@dataclass
class Eval:
    expr: object


@dataclass
class Print:
    args: List[object]     # List[expr]


@dataclass
class If:
    cond: object           # expr
    then_stmt: object      # stmt
    else_stmt: Optional[object] = None  # stmt ou None


@dataclass
class While:
    cond: object           # expr
    body: object           # stmt


@dataclass
class Do:
    body: object           # stmt
    cond: object           # expr


@dataclass
class Assign:
    left: object           # Id | ArrayRef
    right: object          # expr


@dataclass
class Rel:
    op: str                # '<' | '≤'
    left: object           # expr
    right: object          # expr


@dataclass
class Eq:
    op: str                # '==' | '!='
    left: object           # expr
    right: object          # expr


@dataclass
class Lg:
    op: str                # '||' | '&&'
    left: object           # expr
    right: object          # expr


@dataclass
class Unary:
    op: str                # '-' | '!'
    expr: object           # expr


@dataclass
class Ari:
    op: str                # '+' | '-' | '*' | '/'
    left: object           # expr
    right: object          # expr


@dataclass
class NewArray:
    base: str              # 'int' | 'bool'
    size: object           # expr (deve ser int)


@dataclass
class ArrayRef:
    id: "Id"
    index: object          # expr (deve ser int)


@dataclass
class Num:
    value: int


@dataclass
class Bool:
    value: bool


@dataclass
class Id:
    name: str
