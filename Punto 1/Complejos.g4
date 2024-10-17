grammar Complejos;

@header {
    import cmath
}

@members {
    def eval_expr(expr):
        return eval(expr)
}

program
    : expr EOF
    ;

expr
    : expr '+' term    // Suma
    | expr '-' term    // Resta
    | term             // Término
    ;

term
    : COMPLEJO         // NúmeroComplejo
    | REAL             // NúmeroReal
    | '(' expr ')'     // Paréntesis
    ;

COMPLEJO
    : REAL ('+' REAL | '-' REAL) 'i'  // a + bi o a - bi
    | REAL 'i'                         // bi (cuando a es 0)
    ;

REAL
    : [0-9]+ ('.' [0-9]+)?              // Números reales (enteros o decimales)
    ;

WS
    : [ \t\n\r]+ -> skip                 // Espacios en blanco
    ;

