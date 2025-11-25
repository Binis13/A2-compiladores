# Generated from E:\codigos vscode\grammar\MiniLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#stmts.
    def visitStmts(self, ctx:MiniLangParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#stmt.
    def visitStmt(self, ctx:MiniLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#decl.
    def visitDecl(self, ctx:MiniLangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#type_spec.
    def visitType_spec(self, ctx:MiniLangParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#print_stmt.
    def visitPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#while_stmt.
    def visitWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expr_stmt.
    def visitExpr_stmt(self, ctx:MiniLangParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expr.
    def visitExpr(self, ctx:MiniLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#logical_or.
    def visitLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#logical_and.
    def visitLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#equality.
    def visitEquality(self, ctx:MiniLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#relational.
    def visitRelational(self, ctx:MiniLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#additive.
    def visitAdditive(self, ctx:MiniLangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#multiplicative.
    def visitMultiplicative(self, ctx:MiniLangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#unary.
    def visitUnary(self, ctx:MiniLangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#primary.
    def visitPrimary(self, ctx:MiniLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del MiniLangParser