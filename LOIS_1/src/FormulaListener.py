from gen.unclear_coverageParser import unclear_coverageParser
from gen.unclear_coverageListener import unclear_coverageListener


class FormulaListener(unclear_coverageListener):
    def __init__(self):
        self.tuples = []

    def enterSubformula(self, ctx: unclear_coverageParser.SubformulaContext):
        var = ctx.VAR().getText()
        decimal = float(ctx.DECIMAL().getText())
        self.tuples.append((var, decimal))