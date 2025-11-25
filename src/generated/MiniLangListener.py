# Generated from E:\codigos vscode\grammar\MiniLang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#stmts.
    def enterStmts(self, ctx:MiniLangParser.StmtsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stmts.
    def exitStmts(self, ctx:MiniLangParser.StmtsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#stmt.
    def enterStmt(self, ctx:MiniLangParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#stmt.
    def exitStmt(self, ctx:MiniLangParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#decl.
    def enterDecl(self, ctx:MiniLangParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#decl.
    def exitDecl(self, ctx:MiniLangParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type_spec.
    def enterType_spec(self, ctx:MiniLangParser.Type_specContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type_spec.
    def exitType_spec(self, ctx:MiniLangParser.Type_specContext):
        pass


    # Enter a parse tree produced by MiniLangParser#print_stmt.
    def enterPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#print_stmt.
    def exitPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#while_stmt.
    def enterWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#while_stmt.
    def exitWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expr_stmt.
    def enterExpr_stmt(self, ctx:MiniLangParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expr_stmt.
    def exitExpr_stmt(self, ctx:MiniLangParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expr.
    def enterExpr(self, ctx:MiniLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expr.
    def exitExpr(self, ctx:MiniLangParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#logical_or.
    def enterLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        pass

    # Exit a parse tree produced by MiniLangParser#logical_or.
    def exitLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        pass


    # Enter a parse tree produced by MiniLangParser#logical_and.
    def enterLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        pass

    # Exit a parse tree produced by MiniLangParser#logical_and.
    def exitLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        pass


    # Enter a parse tree produced by MiniLangParser#equality.
    def enterEquality(self, ctx:MiniLangParser.EqualityContext):
        pass

    # Exit a parse tree produced by MiniLangParser#equality.
    def exitEquality(self, ctx:MiniLangParser.EqualityContext):
        pass


    # Enter a parse tree produced by MiniLangParser#relational.
    def enterRelational(self, ctx:MiniLangParser.RelationalContext):
        pass

    # Exit a parse tree produced by MiniLangParser#relational.
    def exitRelational(self, ctx:MiniLangParser.RelationalContext):
        pass


    # Enter a parse tree produced by MiniLangParser#additive.
    def enterAdditive(self, ctx:MiniLangParser.AdditiveContext):
        pass

    # Exit a parse tree produced by MiniLangParser#additive.
    def exitAdditive(self, ctx:MiniLangParser.AdditiveContext):
        pass


    # Enter a parse tree produced by MiniLangParser#multiplicative.
    def enterMultiplicative(self, ctx:MiniLangParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#multiplicative.
    def exitMultiplicative(self, ctx:MiniLangParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by MiniLangParser#unary.
    def enterUnary(self, ctx:MiniLangParser.UnaryContext):
        pass

    # Exit a parse tree produced by MiniLangParser#unary.
    def exitUnary(self, ctx:MiniLangParser.UnaryContext):
        pass


    # Enter a parse tree produced by MiniLangParser#primary.
    def enterPrimary(self, ctx:MiniLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MiniLangParser#primary.
    def exitPrimary(self, ctx:MiniLangParser.PrimaryContext):
        pass



del MiniLangParser