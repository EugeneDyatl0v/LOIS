from src.FormulaParser import FormulaParser


class TUPLEException(RuntimeError):
    pass

class UnclearCoverageMaker:

    def t_norm(self, v1, v2):
        return v1 * v2

    def __init__(self, formula_1: str, formula_2: str, premise: str):
        self.tuples_of_formula_1 = FormulaParser.parse_formula(formula_1)
        self.tuples_of_formula_2 = FormulaParser.parse_formula(formula_2)
        self.premise = FormulaParser.parse_formula(premise)
        self.relation = {}
        self.compute_impl()

    def impl(self, element_1, element_2):
        return element_2 / element_1 if element_1 > element_2 else 1

    def compute_impl(self):
        for i in range(len(self.tuples_of_formula_1)):
            self.relation[i] = {}
            for j in range(len(self.tuples_of_formula_2)):
                v1 = self.tuples_of_formula_1[i][1]
                v2 = self.tuples_of_formula_2[j][1]
                self.relation[i][j] = self.impl(v1, v2)

    def conclusion(self):
        conl_set = []
        for i in range(len(self.relation[0])):
            l = []
            for j in range(len(self.relation)):
                v_set = self.premise[j][1]
                v_impl = self.relation[j][i]
                l.append(self.t_norm(v_set, v_impl))
            value = max(l)
            conl_set.append((self.tuples_of_formula_2[i][0], value))
        return conl_set