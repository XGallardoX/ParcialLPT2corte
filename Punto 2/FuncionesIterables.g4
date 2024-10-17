grammar FuncionesIterables;

// Reglas de inicio
prog: (statement)+ EOF;

statement
    : funcMap
    | funcFilter
    ;

funcMap
    : 'MAP' '(' function ',' iterable ')' ';'
    ;

funcFilter
    : 'FILTER' '(' function ',' iterable ')' ';'
    ;

function
    : IDENTIFIER
    ;

iterable
    : list
    | tuple
    ;

list
    : '[' exprList? ']'
    ;

tuple
    : '(' exprList? ')'
    ;

exprList
    : expr (',' expr)*
    ;

expr
    : IDENTIFIER
    | NUMBER
    ;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

NUMBER: '-'?[0-9]+;

WS: [ \t\r\n]+ -> skip;

