# Generated from C:/Users/evgen/PycharmProjects/LOIS_1\unclear_coverage.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,5,0,9,8,0,10,0,12,0,12,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,2,0,2,0,0,20,0,4,1,0,
        0,0,2,15,1,0,0,0,4,5,5,6,0,0,5,10,3,2,1,0,6,7,5,3,0,0,7,9,3,2,1,
        0,8,6,1,0,0,0,9,12,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,0,11,13,1,0,
        0,0,12,10,1,0,0,0,13,14,5,7,0,0,14,1,1,0,0,0,15,16,5,4,0,0,16,17,
        5,2,0,0,17,18,5,3,0,0,18,19,5,1,0,0,19,20,5,5,0,0,20,3,1,0,0,0,1,
        10
    ]

class unclear_coverageParser ( Parser ):

    grammarFileName = "unclear_coverage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "','", "'<'", 
                     "'>'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "DECIMAL", "VAR", "COMMA", "OPENBRACKET", 
                      "CLOSEBRACKET", "OPENFIGURE", "CLOSEFIGURE" ]

    RULE_formula = 0
    RULE_subformula = 1

    ruleNames =  [ "formula", "subformula" ]

    EOF = Token.EOF
    DECIMAL=1
    VAR=2
    COMMA=3
    OPENBRACKET=4
    CLOSEBRACKET=5
    OPENFIGURE=6
    CLOSEFIGURE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENFIGURE(self):
            return self.getToken(unclear_coverageParser.OPENFIGURE, 0)

        def subformula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(unclear_coverageParser.SubformulaContext)
            else:
                return self.getTypedRuleContext(unclear_coverageParser.SubformulaContext,i)


        def CLOSEFIGURE(self):
            return self.getToken(unclear_coverageParser.CLOSEFIGURE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(unclear_coverageParser.COMMA)
            else:
                return self.getToken(unclear_coverageParser.COMMA, i)

        def getRuleIndex(self):
            return unclear_coverageParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula" ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = unclear_coverageParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(unclear_coverageParser.OPENFIGURE)
            self.state = 5
            self.subformula()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 6
                self.match(unclear_coverageParser.COMMA)
                self.state = 7
                self.subformula()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(unclear_coverageParser.CLOSEFIGURE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubformulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENBRACKET(self):
            return self.getToken(unclear_coverageParser.OPENBRACKET, 0)

        def VAR(self):
            return self.getToken(unclear_coverageParser.VAR, 0)

        def COMMA(self):
            return self.getToken(unclear_coverageParser.COMMA, 0)

        def DECIMAL(self):
            return self.getToken(unclear_coverageParser.DECIMAL, 0)

        def CLOSEBRACKET(self):
            return self.getToken(unclear_coverageParser.CLOSEBRACKET, 0)

        def getRuleIndex(self):
            return unclear_coverageParser.RULE_subformula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubformula" ):
                listener.enterSubformula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubformula" ):
                listener.exitSubformula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubformula" ):
                return visitor.visitSubformula(self)
            else:
                return visitor.visitChildren(self)




    def subformula(self):

        localctx = unclear_coverageParser.SubformulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subformula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(unclear_coverageParser.OPENBRACKET)
            self.state = 16
            self.match(unclear_coverageParser.VAR)
            self.state = 17
            self.match(unclear_coverageParser.COMMA)
            self.state = 18
            self.match(unclear_coverageParser.DECIMAL)
            self.state = 19
            self.match(unclear_coverageParser.CLOSEBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





