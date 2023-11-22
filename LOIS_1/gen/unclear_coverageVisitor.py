# Generated from D:/LOIS/LOIS/LOIS_1/unclear_coverage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .unclear_coverageParser import unclear_coverageParser
else:
    from unclear_coverageParser import unclear_coverageParser

# This class defines a complete generic visitor for a parse tree produced by unclear_coverageParser.

class unclear_coverageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by unclear_coverageParser#formula.
    def visitFormula(self, ctx:unclear_coverageParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by unclear_coverageParser#subformula.
    def visitSubformula(self, ctx:unclear_coverageParser.SubformulaContext):
        return self.visitChildren(ctx)



del unclear_coverageParser