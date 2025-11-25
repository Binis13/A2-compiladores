# Generated from E:\codigos vscode\grammar\MiniLang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,1,1,1,3,1,46,8,1,1,1,1,1,1,2,4,2,51,8,2,11,2,12,2,52,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,62,8,3,1,4,3,4,65,8,4,1,4,1,4,1,4,
        3,4,70,8,4,1,4,1,4,1,4,3,4,75,8,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,5,6,86,8,6,10,6,12,6,89,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,101,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,3,11,123,8,11,1,12,1,
        12,1,12,5,12,128,8,12,10,12,12,12,131,9,12,1,13,1,13,1,13,5,13,136,
        8,13,10,13,12,13,139,9,13,1,14,1,14,1,14,5,14,144,8,14,10,14,12,
        14,147,9,14,1,15,1,15,1,15,5,15,152,8,15,10,15,12,15,155,9,15,1,
        16,1,16,1,16,5,16,160,8,16,10,16,12,16,163,9,16,1,17,1,17,1,17,5,
        17,168,8,17,10,17,12,17,171,9,17,1,18,1,18,1,18,3,18,176,8,18,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,186,8,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,198,8,19,1,19,0,0,20,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,6,1,0,10,
        11,1,0,16,17,1,0,18,19,1,0,22,23,1,0,24,25,2,0,21,21,23,23,206,0,
        40,1,0,0,0,2,43,1,0,0,0,4,50,1,0,0,0,6,61,1,0,0,0,8,64,1,0,0,0,10,
        78,1,0,0,0,12,80,1,0,0,0,14,93,1,0,0,0,16,102,1,0,0,0,18,108,1,0,
        0,0,20,116,1,0,0,0,22,119,1,0,0,0,24,124,1,0,0,0,26,132,1,0,0,0,
        28,140,1,0,0,0,30,148,1,0,0,0,32,156,1,0,0,0,34,164,1,0,0,0,36,175,
        1,0,0,0,38,197,1,0,0,0,40,41,3,2,1,0,41,42,5,0,0,1,42,1,1,0,0,0,
        43,45,5,26,0,0,44,46,3,4,2,0,45,44,1,0,0,0,45,46,1,0,0,0,46,47,1,
        0,0,0,47,48,5,27,0,0,48,3,1,0,0,0,49,51,3,6,3,0,50,49,1,0,0,0,51,
        52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,62,3,2,1,
        0,55,62,3,8,4,0,56,62,3,12,6,0,57,62,3,14,7,0,58,62,3,16,8,0,59,
        62,3,18,9,0,60,62,3,20,10,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,
        0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,
        7,1,0,0,0,63,65,5,12,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,
        0,66,69,3,10,5,0,67,68,5,30,0,0,68,70,5,31,0,0,69,67,1,0,0,0,69,
        70,1,0,0,0,70,71,1,0,0,0,71,74,5,35,0,0,72,73,5,20,0,0,73,75,3,22,
        11,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,32,0,0,77,
        9,1,0,0,0,78,79,7,0,0,0,79,11,1,0,0,0,80,81,5,7,0,0,81,82,5,28,0,
        0,82,87,3,22,11,0,83,84,5,33,0,0,84,86,3,22,11,0,85,83,1,0,0,0,86,
        89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,1,0,0,
        0,90,91,5,29,0,0,91,92,5,32,0,0,92,13,1,0,0,0,93,94,5,3,0,0,94,95,
        5,28,0,0,95,96,3,22,11,0,96,97,5,29,0,0,97,100,3,6,3,0,98,99,5,4,
        0,0,99,101,3,6,3,0,100,98,1,0,0,0,100,101,1,0,0,0,101,15,1,0,0,0,
        102,103,5,5,0,0,103,104,5,28,0,0,104,105,3,22,11,0,105,106,5,29,
        0,0,106,107,3,6,3,0,107,17,1,0,0,0,108,109,5,6,0,0,109,110,3,6,3,
        0,110,111,5,5,0,0,111,112,5,28,0,0,112,113,3,22,11,0,113,114,5,29,
        0,0,114,115,5,32,0,0,115,19,1,0,0,0,116,117,3,22,11,0,117,118,5,
        32,0,0,118,21,1,0,0,0,119,122,3,24,12,0,120,121,5,20,0,0,121,123,
        3,22,11,0,122,120,1,0,0,0,122,123,1,0,0,0,123,23,1,0,0,0,124,129,
        3,26,13,0,125,126,5,15,0,0,126,128,3,26,13,0,127,125,1,0,0,0,128,
        131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,25,1,0,0,0,131,129,
        1,0,0,0,132,137,3,28,14,0,133,134,5,14,0,0,134,136,3,28,14,0,135,
        133,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,
        27,1,0,0,0,139,137,1,0,0,0,140,145,3,30,15,0,141,142,7,1,0,0,142,
        144,3,30,15,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,
        146,1,0,0,0,146,29,1,0,0,0,147,145,1,0,0,0,148,153,3,32,16,0,149,
        150,7,2,0,0,150,152,3,32,16,0,151,149,1,0,0,0,152,155,1,0,0,0,153,
        151,1,0,0,0,153,154,1,0,0,0,154,31,1,0,0,0,155,153,1,0,0,0,156,161,
        3,34,17,0,157,158,7,3,0,0,158,160,3,34,17,0,159,157,1,0,0,0,160,
        163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,33,1,0,0,0,163,161,
        1,0,0,0,164,169,3,36,18,0,165,166,7,4,0,0,166,168,3,36,18,0,167,
        165,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,
        35,1,0,0,0,171,169,1,0,0,0,172,173,7,5,0,0,173,176,3,36,18,0,174,
        176,3,38,19,0,175,172,1,0,0,0,175,174,1,0,0,0,176,37,1,0,0,0,177,
        198,5,34,0,0,178,198,5,8,0,0,179,198,5,9,0,0,180,185,5,35,0,0,181,
        182,5,30,0,0,182,183,3,22,11,0,183,184,5,31,0,0,184,186,1,0,0,0,
        185,181,1,0,0,0,185,186,1,0,0,0,186,198,1,0,0,0,187,188,5,28,0,0,
        188,189,3,22,11,0,189,190,5,29,0,0,190,198,1,0,0,0,191,192,5,13,
        0,0,192,193,3,10,5,0,193,194,5,30,0,0,194,195,3,22,11,0,195,196,
        5,31,0,0,196,198,1,0,0,0,197,177,1,0,0,0,197,178,1,0,0,0,197,179,
        1,0,0,0,197,180,1,0,0,0,197,187,1,0,0,0,197,191,1,0,0,0,198,39,1,
        0,0,0,18,45,52,61,64,69,74,87,100,122,129,137,145,153,161,169,175,
        185,197
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'while'", "'do'", "'print'", "'true'", "'false'", 
                     "'int'", "'bool'", "'const'", "'new'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<='", "'<'", "'='", "'!'", "'+'", 
                     "'-'", "'*'", "'/'", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "LINECOMMENT", "BLOCKCOMMENT", "IF", 
                      "ELSE", "WHILE", "DO", "PRINT", "TRUE", "FALSE", "INT_KW", 
                      "BOOL_KW", "CONST", "NEW", "ANDAND", "OROR", "EQEQ", 
                      "NE", "LE", "LT", "ASSIGN", "NOT", "PLUS", "MINUS", 
                      "TIMES", "DIV", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "NUM", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_block = 1
    RULE_stmts = 2
    RULE_stmt = 3
    RULE_decl = 4
    RULE_type_spec = 5
    RULE_print_stmt = 6
    RULE_if_stmt = 7
    RULE_while_stmt = 8
    RULE_do_while_stmt = 9
    RULE_expr_stmt = 10
    RULE_expr = 11
    RULE_logical_or = 12
    RULE_logical_and = 13
    RULE_equality = 14
    RULE_relational = 15
    RULE_additive = 16
    RULE_multiplicative = 17
    RULE_unary = 18
    RULE_primary = 19

    ruleNames =  [ "program", "block", "stmts", "stmt", "decl", "type_spec", 
                   "print_stmt", "if_stmt", "while_stmt", "do_while_stmt", 
                   "expr_stmt", "expr", "logical_or", "logical_and", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "primary" ]

    EOF = Token.EOF
    LINECOMMENT=1
    BLOCKCOMMENT=2
    IF=3
    ELSE=4
    WHILE=5
    DO=6
    PRINT=7
    TRUE=8
    FALSE=9
    INT_KW=10
    BOOL_KW=11
    CONST=12
    NEW=13
    ANDAND=14
    OROR=15
    EQEQ=16
    NE=17
    LE=18
    LT=19
    ASSIGN=20
    NOT=21
    PLUS=22
    MINUS=23
    TIMES=24
    DIV=25
    LBRACE=26
    RBRACE=27
    LPAREN=28
    RPAREN=29
    LBRACK=30
    RBRACK=31
    SEMI=32
    COMMA=33
    NUM=34
    ID=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.block()
            self.state = 41
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniLangParser.RBRACE, 0)

        def stmts(self):
            return self.getTypedRuleContext(MiniLangParser.StmtsContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiniLangParser.LBRACE)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 51885653992) != 0):
                self.state = 44
                self.stmts()


            self.state = 47
            self.match(MiniLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = MiniLangParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.stmt()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 51885653992) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def decl(self):
            return self.getTypedRuleContext(MiniLangParser.DeclContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.Print_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.Do_while_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.block()
                pass
            elif token in [10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.decl()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.print_stmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.if_stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.while_stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.do_while_stmt()
                pass
            elif token in [8, 9, 13, 21, 23, 28, 34, 35]:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.expr_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_spec(self):
            return self.getTypedRuleContext(MiniLangParser.Type_specContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def CONST(self):
            return self.getToken(MiniLangParser.CONST, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 63
                self.match(MiniLangParser.CONST)


            self.state = 66
            self.type_spec()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 67
                self.match(MiniLangParser.LBRACK)
                self.state = 68
                self.match(MiniLangParser.RBRACK)


            self.state = 71
            self.match(MiniLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 72
                self.match(MiniLangParser.ASSIGN)
                self.state = 73
                self.expr()


            self.state = 76
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_KW(self):
            return self.getToken(MiniLangParser.INT_KW, 0)

        def BOOL_KW(self):
            return self.getToken(MiniLangParser.BOOL_KW, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_type_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_spec" ):
                listener.enterType_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_spec" ):
                listener.exitType_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = MiniLangParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_spec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniLangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = MiniLangParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MiniLangParser.PRINT)
            self.state = 81
            self.match(MiniLangParser.LPAREN)
            self.state = 82
            self.expr()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 83
                self.match(MiniLangParser.COMMA)
                self.state = 84
                self.expr()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(MiniLangParser.RPAREN)
            self.state = 91
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(MiniLangParser.IF)
            self.state = 94
            self.match(MiniLangParser.LPAREN)
            self.state = 95
            self.expr()
            self.state = 96
            self.match(MiniLangParser.RPAREN)
            self.state = 97
            self.stmt()
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 98
                self.match(MiniLangParser.ELSE)
                self.state = 99
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(MiniLangParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MiniLangParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MiniLangParser.WHILE)
            self.state = 103
            self.match(MiniLangParser.LPAREN)
            self.state = 104
            self.expr()
            self.state = 105
            self.match(MiniLangParser.RPAREN)
            self.state = 106
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MiniLangParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(MiniLangParser.StmtContext,0)


        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_do_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_stmt" ):
                listener.enterDo_while_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_stmt" ):
                listener.exitDo_while_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MiniLangParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MiniLangParser.DO)
            self.state = 109
            self.stmt()
            self.state = 110
            self.match(MiniLangParser.WHILE)
            self.state = 111
            self.match(MiniLangParser.LPAREN)
            self.state = 112
            self.expr()
            self.state = 113
            self.match(MiniLangParser.RPAREN)
            self.state = 114
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_expr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_stmt" ):
                listener.enterExpr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_stmt" ):
                listener.exitExpr_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = MiniLangParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expr()
            self.state = 117
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_or(self):
            return self.getTypedRuleContext(MiniLangParser.Logical_orContext,0)


        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.logical_or()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 120
                self.match(MiniLangParser.ASSIGN)
                self.state = 121
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.Logical_andContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.Logical_andContext,i)


        def OROR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.OROR)
            else:
                return self.getToken(MiniLangParser.OROR, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_logical_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_or" ):
                listener.enterLogical_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_or" ):
                listener.exitLogical_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_or" ):
                return visitor.visitLogical_or(self)
            else:
                return visitor.visitChildren(self)




    def logical_or(self):

        localctx = MiniLangParser.Logical_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logical_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.logical_and()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 125
                self.match(MiniLangParser.OROR)
                self.state = 126
                self.logical_and()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.EqualityContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.EqualityContext,i)


        def ANDAND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ANDAND)
            else:
                return self.getToken(MiniLangParser.ANDAND, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_logical_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_and" ):
                listener.enterLogical_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_and" ):
                listener.exitLogical_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and" ):
                return visitor.visitLogical_and(self)
            else:
                return visitor.visitChildren(self)




    def logical_and(self):

        localctx = MiniLangParser.Logical_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logical_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.equality()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 133
                self.match(MiniLangParser.ANDAND)
                self.state = 134
                self.equality()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.RelationalContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.RelationalContext,i)


        def EQEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.EQEQ)
            else:
                return self.getToken(MiniLangParser.EQEQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NE)
            else:
                return self.getToken(MiniLangParser.NE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = MiniLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.relational()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.relational()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AdditiveContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LT)
            else:
                return self.getToken(MiniLangParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LE)
            else:
                return self.getToken(MiniLangParser.LE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MiniLangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.additive()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.additive()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.PLUS)
            else:
                return self.getToken(MiniLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MINUS)
            else:
                return self.getToken(MiniLangParser.MINUS, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = MiniLangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.multiplicative()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.multiplicative()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.UnaryContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.UnaryContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.TIMES)
            else:
                return self.getToken(MiniLangParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.DIV)
            else:
                return self.getToken(MiniLangParser.DIV, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = MiniLangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.unary()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.unary()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MiniLangParser.UnaryContext,0)


        def NOT(self):
            return self.getToken(MiniLangParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniLangParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(MiniLangParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniLangParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==21 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.unary()
                pass
            elif token in [8, 9, 13, 28, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(MiniLangParser.NUM, 0)

        def TRUE(self):
            return self.getToken(MiniLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniLangParser.FALSE, 0)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def NEW(self):
            return self.getToken(MiniLangParser.NEW, 0)

        def type_spec(self):
            return self.getTypedRuleContext(MiniLangParser.Type_specContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MiniLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(MiniLangParser.NUM)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(MiniLangParser.TRUE)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(MiniLangParser.FALSE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.match(MiniLangParser.ID)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 181
                    self.match(MiniLangParser.LBRACK)
                    self.state = 182
                    self.expr()
                    self.state = 183
                    self.match(MiniLangParser.RBRACK)


                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.match(MiniLangParser.LPAREN)
                self.state = 188
                self.expr()
                self.state = 189
                self.match(MiniLangParser.RPAREN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 191
                self.match(MiniLangParser.NEW)
                self.state = 192
                self.type_spec()
                self.state = 193
                self.match(MiniLangParser.LBRACK)
                self.state = 194
                self.expr()
                self.state = 195
                self.match(MiniLangParser.RBRACK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





