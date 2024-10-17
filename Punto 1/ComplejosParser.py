# Generated from Complejos.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import cmath
import sys

if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,30,8,2,1,2,0,1,2,3,0,2,4,0,0,32,0,6,1,0,0,0,2,9,1,0,0,0,
        4,29,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,
        11,3,4,2,0,11,20,1,0,0,0,12,13,10,3,0,0,13,14,5,1,0,0,14,19,3,4,
        2,0,15,16,10,2,0,0,16,17,5,2,0,0,17,19,3,4,2,0,18,12,1,0,0,0,18,
        15,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,
        0,22,20,1,0,0,0,23,30,5,5,0,0,24,30,5,6,0,0,25,26,5,3,0,0,26,27,
        3,2,1,0,27,28,5,4,0,0,28,30,1,0,0,0,29,23,1,0,0,0,29,24,1,0,0,0,
        29,25,1,0,0,0,30,5,1,0,0,0,3,18,20,29
    ]

class ComplejosParser ( Parser ):

    grammarFileName = "Complejos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMPLEJO", "REAL", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_term = 2

    ruleNames =  [ "program", "expr", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    COMPLEJO=5
    REAL=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        def eval_expr(expr):
            return eval(expr)



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ComplejosParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ComplejosParser.EOF, 0)

        def getRuleIndex(self):
            return ComplejosParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ComplejosParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr(0)
            self.state = 7
            self.match(ComplejosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ComplejosParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(ComplejosParser.ExprContext,0)


        def getRuleIndex(self):
            return ComplejosParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplejosParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ComplejosParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 13
                        self.match(ComplejosParser.T__0)
                        self.state = 14
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = ComplejosParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 16
                        self.match(ComplejosParser.T__1)
                        self.state = 17
                        self.term()
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPLEJO(self):
            return self.getToken(ComplejosParser.COMPLEJO, 0)

        def REAL(self):
            return self.getToken(ComplejosParser.REAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ComplejosParser.ExprContext,0)


        def getRuleIndex(self):
            return ComplejosParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ComplejosParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ComplejosParser.COMPLEJO)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(ComplejosParser.REAL)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(ComplejosParser.T__2)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(ComplejosParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




