# -*- coding: utf-8 -*-
"""
Construtor de AST: converte o parse tree do ANTLR para nossa AST.
"""
import sys
import os
from typing import Any, List

# Adiciona src/generated ao path para encontrar o código gerado do ANTLR
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

try:
    from MiniLangParser import MiniLangParser
    from MiniLangVisitor import MiniLangVisitor
except ImportError:
    # Se os imports falharem, serão tratados quando ast_builder for importado
    MiniLangParser = None
    MiniLangVisitor = None

from .ast_nodes import *


class ASTBuilder(MiniLangVisitor if MiniLangVisitor else object):
    """Visitor que constrói a AST a partir do parse tree do ANTLR."""

    def visitProgram(self, ctx):
        """program: block;"""
        block = self.visit(ctx.block())
        return Program(block)

    def visitBlock(self, ctx):
        """block: LBRACE stmts RBRACE;"""
        stmts = None
        if ctx.stmts():
            stmts = self.visit(ctx.stmts())
        return Block(stmts)

    def visitStmts(self, ctx):
        """stmts: stmt+;"""
        return [self.visit(stmt) for stmt in ctx.stmt()]

    def visitStmt(self, ctx):
        """stmt: block | decl | print_stmt | if_stmt | while_stmt | do_while_stmt | expr_stmt;"""
        if ctx.block():
            return self.visit(ctx.block())
        if ctx.decl():
            return self.visit(ctx.decl())
        if ctx.print_stmt():
            return self.visit(ctx.print_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        if ctx.expr_stmt():
            return self.visit(ctx.expr_stmt())
        return None

    def visitDecl(self, ctx):
        """decl: (CONST)? type_spec ID (LBRACK RBRACK)? (ASSIGN expr)? SEMI;"""
        is_const = ctx.CONST() is not None
        type_spec = ctx.type_spec().getText()
        is_array = ctx.LBRACK() is not None
        id_node = Id(ctx.ID().getText())
        init_expr = None
        if ctx.expr():
            init_expr = self.visit(ctx.expr())
        return Decl(type_spec, is_array, is_const, id_node, init_expr)

    def visitPrint_stmt(self, ctx):
        """print_stmt: PRINT LPAREN expr (COMMA expr)* RPAREN SEMI;"""
        args = [self.visit(expr) for expr in ctx.expr()]
        return Print(args)

    def visitIf_stmt(self, ctx):
        """if_stmt: IF LPAREN expr RPAREN stmt (ELSE stmt)?;"""
        cond = self.visit(ctx.expr())
        stmts = ctx.stmt()
        then_stmt = self.visit(stmts[0])
        else_stmt = None
        if len(stmts) > 1:
            else_stmt = self.visit(stmts[1])
        return If(cond, then_stmt, else_stmt)

    def visitWhile_stmt(self, ctx):
        """while_stmt: WHILE LPAREN expr RPAREN stmt;"""
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.stmt())
        return While(cond, body)

    def visitDo_while_stmt(self, ctx):
        """do_while_stmt: DO stmt WHILE LPAREN expr RPAREN SEMI;"""
        body = self.visit(ctx.stmt())
        cond = self.visit(ctx.expr())
        return Do(body, cond)

    def visitExpr_stmt(self, ctx):
        """expr_stmt: expr SEMI;"""
        expr = self.visit(ctx.expr())
        return Eval(expr)

    # Expressions
    def visitExpr(self, ctx):
        """expr: logical_or (ASSIGN expr)?;"""
        left = self.visit(ctx.logical_or())
        if ctx.ASSIGN():
            right = self.visit(ctx.expr())
            return Assign(left, right)
        return left

    def visitLogical_or(self, ctx):
        """logical_or: logical_and (OR logical_and)*;"""
        logicals = ctx.logical_and()
        node = self.visit(logicals[0])
        for i in range(1, len(logicals)):
            node = Lg("||", node, self.visit(logicals[i]))
        return node

    def visitLogical_and(self, ctx):
        """logical_and: equality (AND equality)*;"""
        equalities = ctx.equality()
        node = self.visit(equalities[0])
        for i in range(1, len(equalities)):
            node = Lg("&&", node, self.visit(equalities[i]))
        return node

    def visitEquality(self, ctx):
        """equality: relational ((EQEQ | NE) relational)*;"""
        relationals = ctx.relational()
        node = self.visit(relationals[0])
        
        # Coleta operadores
        ops = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'symbol'):
                text = child.getText()
                if text in ["==", "!="]:
                    ops.append(text)
        
        for i, op in enumerate(ops):
            node = Eq(op, node, self.visit(relationals[i + 1]))
        return node

    def visitRelational(self, ctx):
        """relational: additive ((LT | LE) additive)*;"""
        additives = ctx.additive()
        node = self.visit(additives[0])
        
        # Coleta operadores
        ops = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'symbol'):
                text = child.getText()
                if text in ["<", "<="]:
                    ops.append(text)
        
        for i, op in enumerate(ops):
            # Mantém operador como está (não converte para ≤)
            node = Rel(op, node, self.visit(additives[i + 1]))
        return node

    def visitAdditive(self, ctx):
        """additive: multiplicative ((PLUS | MINUS) multiplicative)*;"""
        multiplicatives = ctx.multiplicative()
        node = self.visit(multiplicatives[0])
        
        # Coleta operadores
        ops = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'symbol'):
                text = child.getText()
                if text in ["+", "-"]:
                    ops.append(text)
        
        for i, op in enumerate(ops):
            node = Ari(op, node, self.visit(multiplicatives[i + 1]))
        return node

    def visitMultiplicative(self, ctx):
        """multiplicative: unary ((MUL | DIV) unary)*;"""
        unaries = ctx.unary()
        node = self.visit(unaries[0])
        
        # Coleta operadores
        ops = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'symbol'):
                text = child.getText()
                if text in ["*", "/"]:
                    ops.append(text)
        
        for i, op in enumerate(ops):
            node = Ari(op, node, self.visit(unaries[i + 1]))
        return node

    def visitUnary(self, ctx):
        """unary: (NOT | MINUS) unary | primary;"""
        if ctx.NOT():
            return Unary("!", self.visit(ctx.unary()))
        if ctx.MINUS():
            unary_part = self.visit(ctx.unary())
            if isinstance(unary_part, Num):
                return Num(-unary_part.value)
            return Unary("-", unary_part)
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx):
        """primary: NUM | TRUE | FALSE | ID (LBRACK expr RBRACK)? | LPAREN expr RPAREN | NEW type_spec LBRACK expr RBRACK;"""
        if ctx.NUM():
            return Num(int(ctx.NUM().getText()))
        if ctx.TRUE():
            return Bool(True)
        if ctx.FALSE():
            return Bool(False)
        if ctx.ID():
            id_text = ctx.ID().getText()
            if ctx.LBRACK():
                # ID[expr]
                idx = self.visit(ctx.expr())
                return ArrayRef(Id(id_text), idx)
            return Id(id_text)
        if ctx.NEW():
            # new type_spec[expr]
            base = ctx.type_spec().getText()
            size = self.visit(ctx.expr())
            return NewArray(base, size)
        # LPAREN expr RPAREN
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def defaultResult(self):
        """Resultado padrão se nenhum método visit for chamado."""
        return None
