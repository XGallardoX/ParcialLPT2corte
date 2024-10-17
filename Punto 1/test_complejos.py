import cmath
from antlr4 import *
from ComplejosLexer import ComplejosLexer
from ComplejosParser import ComplejosParser

# Función para evaluar una expresión compleja
def eval_expr(expr):
    return eval(expr.replace('i', 'j'))

def main():
    # Lee la expresión de la entrada
    input_expr = input("Ingresa la expresión con números complejos: ")

    # Crea un InputStream
    input_stream = InputStream(input_expr)

    # Inicializa el lexer y el parser
    lexer = ComplejosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplejosParser(stream)

    # Realiza el parseo
    tree = parser.program()

    # Evaluar la expresión usando Python
    resultado = eval_expr(input_expr)
    print("Resultado:", resultado)

if __name__ == '__main__':
    main()

