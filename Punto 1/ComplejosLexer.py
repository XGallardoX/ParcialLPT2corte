# Generated from Complejos.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


    import cmath


def serializedATN():
    return [
        4,0,7,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,29,
        8,4,1,4,1,4,1,4,1,4,1,4,3,4,36,8,4,1,5,4,5,39,8,5,11,5,12,5,40,1,
        5,1,5,4,5,45,8,5,11,5,12,5,46,3,5,49,8,5,1,6,4,6,52,8,6,11,6,12,
        6,53,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,
        3,0,9,10,13,13,32,32,62,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,
        1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,9,35,1,0,0,0,11,38,1,0,0,0,13,
        51,1,0,0,0,15,16,5,43,0,0,16,2,1,0,0,0,17,18,5,45,0,0,18,4,1,0,0,
        0,19,20,5,40,0,0,20,6,1,0,0,0,21,22,5,41,0,0,22,8,1,0,0,0,23,28,
        3,11,5,0,24,25,5,43,0,0,25,29,3,11,5,0,26,27,5,45,0,0,27,29,3,11,
        5,0,28,24,1,0,0,0,28,26,1,0,0,0,29,30,1,0,0,0,30,31,5,105,0,0,31,
        36,1,0,0,0,32,33,3,11,5,0,33,34,5,105,0,0,34,36,1,0,0,0,35,23,1,
        0,0,0,35,32,1,0,0,0,36,10,1,0,0,0,37,39,7,0,0,0,38,37,1,0,0,0,39,
        40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,48,1,0,0,0,42,44,5,46,
        0,0,43,45,7,0,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,49,1,0,0,0,48,42,1,0,0,0,48,49,1,0,0,0,49,12,1,0,0,0,
        50,52,7,1,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,
        0,0,0,54,55,1,0,0,0,55,56,6,6,0,0,56,14,1,0,0,0,7,0,28,35,40,46,
        48,53,1,6,0,0
    ]

class ComplejosLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    COMPLEJO = 5
    REAL = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "COMPLEJO", "REAL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "COMPLEJO", "REAL", "WS" ]

    grammarFileName = "Complejos.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        def eval_expr(expr):
            return eval(expr)


