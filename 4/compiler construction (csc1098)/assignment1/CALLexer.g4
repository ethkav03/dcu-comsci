lexer grammar CALLexer;

VARIABLE: 'variable';
CONSTANT: 'constant';
RETURN: 'return';
INT: 'int';
BOOL: 'bool';
VOID: 'void';
MAIN: 'main';
IF: 'if';
ELSE: 'else';
TRUE: 'true';
FALSE: 'false';
WHILE: 'while';
BEGIN: 'begin';
END: 'end';
IS: 'is';
SKIP: 'skip';

PLUS: '+';
MINUS: '-';
ASSIGN: ':=';
COMMA: ',';
SEMI: ';';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
AND: '&';
OR: '|';
NOT: '~';
EQ: '=';
NEQ: '!=';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';

INTEGER: '-'? [0-9]+;
IDENTIFIER: [a-zA-Z] [a-zA-Z0-9_]*;

COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
