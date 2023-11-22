# Generated from D:/LOIS/LOIS/LOIS_1/unclear_coverage.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,4,0,21,8,0,11,0,12,0,22,3,0,25,8,0,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,0,0,7,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,1,0,2,1,0,48,57,1,0,65,90,39,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,1,24,1,0,0,0,3,26,1,0,0,0,5,28,1,0,0,0,7,30,1,0,0,0,9,32,1,0,0,
        0,11,34,1,0,0,0,13,36,1,0,0,0,15,25,2,48,49,0,16,17,5,48,0,0,17,
        18,5,46,0,0,18,20,1,0,0,0,19,21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,
        0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,15,1,0,0,0,24,16,
        1,0,0,0,25,2,1,0,0,0,26,27,7,1,0,0,27,4,1,0,0,0,28,29,5,44,0,0,29,
        6,1,0,0,0,30,31,5,60,0,0,31,8,1,0,0,0,32,33,5,62,0,0,33,10,1,0,0,
        0,34,35,5,123,0,0,35,12,1,0,0,0,36,37,5,125,0,0,37,14,1,0,0,0,3,
        0,22,24,0
    ]

class unclear_coverageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DECIMAL = 1
    VAR = 2
    COMMA = 3
    OPENBRACKET = 4
    CLOSEBRACKET = 5
    OPENFIGURE = 6
    CLOSEFIGURE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'<'", "'>'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "DECIMAL", "VAR", "COMMA", "OPENBRACKET", "CLOSEBRACKET", "OPENFIGURE", 
            "CLOSEFIGURE" ]

    ruleNames = [ "DECIMAL", "VAR", "COMMA", "OPENBRACKET", "CLOSEBRACKET", 
                  "OPENFIGURE", "CLOSEFIGURE" ]

    grammarFileName = "unclear_coverage.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


