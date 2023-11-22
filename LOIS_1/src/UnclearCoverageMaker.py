from src.FormulaParser import FormulaParser


class UnclearCoverageMaker:

    def t_norm(self, v1, v2):
        return min(v1, v2)

    def __init__(self, formula_1: str, formula_2: str):
        self.tuples_of_formula_1 = FormulaParser.parse_formula(formula_1)
        self.tuples_of_formula_2 = FormulaParser.parse_formula(formula_2)
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
        for i in self.relation:
            l = []
            for j in self.relation[i]:
                v_set = self.tuples_of_formula_2[i][1]
                v_impl = self.relation[i][j]
                l.append(self.t_norm(v_set, v_impl))
            value = max(l)
            conl_set.append((self.tuples_of_formula_2[i][0], value))
        return conl_set