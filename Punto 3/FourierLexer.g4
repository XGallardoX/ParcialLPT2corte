lexer grammar FourierLexer;

FOURIER_TRANSFORM : 'fourier_transform';
INVERSE_TRANSFORM : 'inverse_fourier_transform';
GET_TRANSFORM_PAIR: 'get_transform_pair';
PLUS              : '+';
MINUS             : '-';
MULT              : '*';
DIV               : '/';
PI                : 'pi';
EULER             : 'euler';
SIN               : 'sin';
COS               : 'cos';
LPAREN            : '(';
RPAREN            : ')';
LBRACK            : '[';
RBRACK            : ']';
COMMA             : ',';
NUMBER            : [0-9]+ ('.' [0-9]+)?;
WS                : [ \t\r\n]+ -> skip;

