grammar MiniLang;

// Lexer rules (tokens)

// Comments
LINECOMMENT  : '//' ~[\r\n]* -> skip;
BLOCKCOMMENT : '/*' .*? '*/' -> skip;

// Keywords
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
DO      : 'do';
PRINT   : 'print';
TRUE    : 'true';
FALSE   : 'false';
INT_KW  : 'int';
BOOL_KW : 'bool';
CONST   : 'const';
NEW     : 'new';

// Operators and Delimiters
ANDAND  : '&&';
OROR    : '||';
EQEQ    : '==';
NE      : '!=';
LE      : '<=';
LT      : '<';
ASSIGN  : '=';
NOT     : '!';
PLUS    : '+';
MINUS   : '-';
TIMES   : '*';
DIV     : '/';
LBRACE  : '{';
RBRACE  : '}';
LPAREN  : '(';
RPAREN  : ')';
LBRACK  : '[';
RBRACK  : ']';
SEMI    : ';';
COMMA   : ',';

// Literals
NUM     : [0-9]+;
ID      : [a-zA-Z_][a-zA-Z0-9_]*;

// Whitespace
WS      : [ \t\r\n]+ -> skip;

// Parser rules

program
    : block EOF
    ;

block
    : LBRACE stmts? RBRACE
    ;

stmts
    : stmt+
    ;

stmt
    : block
    | decl
    | print_stmt
    | if_stmt
    | while_stmt
    | do_while_stmt
    | expr_stmt
    ;

decl
    : CONST? type_spec (LBRACK RBRACK)? ID (ASSIGN expr)? SEMI
    ;

type_spec
    : INT_KW
    | BOOL_KW
    ;

print_stmt
    : PRINT LPAREN expr (COMMA expr)* RPAREN SEMI
    ;

if_stmt
    : IF LPAREN expr RPAREN stmt (ELSE stmt)?
    ;

while_stmt
    : WHILE LPAREN expr RPAREN stmt
    ;

do_while_stmt
    : DO stmt WHILE LPAREN expr RPAREN SEMI
    ;

expr_stmt
    : expr SEMI
    ;

// Expressions (precedence: weakest to strongest)
expr
    : logical_or (ASSIGN expr)?
    ;

logical_or
    : logical_and (OROR logical_and)*
    ;

logical_and
    : equality (ANDAND equality)*
    ;

equality
    : relational ((EQEQ | NE) relational)*
    ;

relational
    : additive ((LT | LE) additive)*
    ;

additive
    : multiplicative ((PLUS | MINUS) multiplicative)*
    ;

multiplicative
    : unary ((TIMES | DIV) unary)*
    ;

unary
    : (NOT | MINUS) unary
    | primary
    ;

primary
    : NUM
    | TRUE
    | FALSE
    | ID (LBRACK expr RBRACK)?
    | LPAREN expr RPAREN
    | NEW type_spec LBRACK expr RBRACK
    ;
