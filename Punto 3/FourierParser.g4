parser grammar FourierParser;

options { tokenVocab=FourierLexer; }

program : statement+ ;

statement 
    : fourierTransform     # FourierTransformStatement
    | inverseTransform     # InverseTransformStatement
    | transformPair        # TransformPairStatement
    | expr                 # ArithmeticExpressionStatement
    ;

fourierTransform : FOURIER_TRANSFORM LPAREN list RPAREN ;
inverseTransform : INVERSE_TRANSFORM LPAREN list RPAREN ;
transformPair    : GET_TRANSFORM_PAIR LPAREN NUMBER RPAREN ;

list : LBRACK expr (COMMA expr)* RBRACK ;

expr
    : expr PLUS expr        # addition
    | expr MINUS expr       # subtraction
    | expr MULT expr        # multiplication
    | expr DIV expr         # division
    | SIN LPAREN expr RPAREN # sinFunction
    | COS LPAREN expr RPAREN # cosFunction
    | PI                    # piConstant
    | EULER                 # eulerConstant
    | NUMBER                # number
    | LPAREN expr RPAREN    # parentheses
    ;

