from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.unclear_coverageLexer import unclear_coverageLexer
from gen.unclear_coverageParser import unclear_coverageParser
from src.FormulaListener import FormulaListener

class FormulaParser:
    @staticmethod
    def parse_formula(input_str):
        lexer = unclear_coverageLexer(InputStream(input_str))
        stream = CommonTokenStream(lexer)
        parser = unclear_coverageParser(stream)
        tree = parser.formula()

        listener = FormulaListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        return listener.tuples

