# Generated from Complejos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplejosParser import ComplejosParser
else:
    from ComplejosParser import ComplejosParser

    import cmath


# This class defines a complete listener for a parse tree produced by ComplejosParser.
class ComplejosListener(ParseTreeListener):

    # Enter a parse tree produced by ComplejosParser#program.
    def enterProgram(self, ctx:ComplejosParser.ProgramContext):
        pass

    # Exit a parse tree produced by ComplejosParser#program.
    def exitProgram(self, ctx:ComplejosParser.ProgramContext):
        pass


    # Enter a parse tree produced by ComplejosParser#expr.
    def enterExpr(self, ctx:ComplejosParser.ExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#expr.
    def exitExpr(self, ctx:ComplejosParser.ExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#term.
    def enterTerm(self, ctx:ComplejosParser.TermContext):
        pass

    # Exit a parse tree produced by ComplejosParser#term.
    def exitTerm(self, ctx:ComplejosParser.TermContext):
        pass



del ComplejosParser