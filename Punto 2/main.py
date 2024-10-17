import sys
from antlr4 import *
from FuncionesIterablesLexer import FuncionesIterablesLexer
from FuncionesIterablesParser import FuncionesIterablesParser

# Definir las funciones que se utilizarán en el MAP y FILTER
def multiply(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

# Función para ejecutar MAP
def ejecutar_map(func, iterable):
    return list(map(func, iterable))

# Función para ejecutar FILTER
def ejecutar_filter(func, iterable):
    return list(filter(func, iterable))

# Listener personalizado para manejar MAP y FILTER
class FuncionesIterablesListener(ParseTreeListener):
    def __init__(self):
        self.funciones = {
            'multiply': multiply,
            'is_even': is_even
        }

    def enterFuncMap(self, ctx: FuncionesIterablesParser.FuncMapContext):
        func_name = ctx.function().getText()
        iterable = eval(ctx.iterable().getText())  # Evaluamos la lista o tupla
        resultado = ejecutar_map(self.funciones[func_name], iterable)
        print(f"Resultado de MAP({func_name}, {iterable}): {resultado}")

    def enterFuncFilter(self, ctx: FuncionesIterablesParser.FuncFilterContext):
        func_name = ctx.function().getText()
        iterable = eval(ctx.iterable().getText())  # Evaluamos la lista o tupla
        resultado = ejecutar_filter(self.funciones[func_name], iterable)
        print(f"Resultado de FILTER({func_name}, {iterable}): {resultado}")

# Función principal para parsear la entrada
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = FuncionesIterablesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FuncionesIterablesParser(stream)
    tree = parser.prog()

    # Configurar el listener
    listener = FuncionesIterablesListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)

