import sys
from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser
from FourierVisitorImpl import FourierVisitorImpl

# Ejecutar el programa con la entrada ANTLR
def main(input_file):
    input_stream = FileStream(input_file)
    lexer = FourierLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FourierParser(stream)
    
    tree = parser.program()

    # Crear e invocar el Visitor
    visitor = FourierVisitorImpl()
    visitor.visit(tree)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    main(input_file)

