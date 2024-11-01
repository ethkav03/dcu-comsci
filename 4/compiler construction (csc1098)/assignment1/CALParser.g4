parser grammar CALParser;

options { tokenVocab=CALLexer; }

program: declList functionList main;

declList: (decl SEMI declList | /* epsilon */);
decl: varDecl | constDecl;

varDecl: VARIABLE IDENTIFIER COLON type;
constDecl: CONSTANT IDENTIFIER COLON type ASSIGN expression;

functionList: (function functionList | /* epsilon */);
function: type IDENTIFIER LPAREN parameterList RPAREN IS declList BEGIN statementBlock RETURN (expression | /* epsilon */) SEMI END;

type: INT | BOOL | VOID;
parameterList: (nonEmptyParameterList | /* epsilon */);
nonEmptyParameterList: IDENTIFIER COLON type (COMMA nonEmptyParameterList)?;

main: MAIN BEGIN declList statementBlock END;

statementBlock: (statement statementBlock | /* epsilon */);
statement: IDENTIFIER ASSIGN expression SEMI
         | IDENTIFIER LPAREN argList RPAREN SEMI
         | BEGIN statementBlock END
         | IF condition BEGIN statementBlock END ELSE BEGIN statementBlock END
         | WHILE condition BEGIN statementBlock END
         | SKIP SEMI;

expression: fragment binaryArithOp fragment
          | LPAREN expression RPAREN
          | IDENTIFIER LPAREN argList RPAREN;

fragment: IDENTIFIER | MINUS IDENTIFIER | INTEGER | TRUE | FALSE | LPAREN expression RPAREN;

condition: NOT condition
         | LPAREN condition RPAREN
         | expression compOp expression
         | condition (OR | AND) condition;

compOp: EQ | NEQ | LT | LEQ | GT | GEQ;
argList: (nonEmptyArgList | /* epsilon */);
nonEmptyArgList: IDENTIFIER (COMMA nonEmptyArgList)?;
