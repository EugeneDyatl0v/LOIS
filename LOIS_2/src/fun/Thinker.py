from src.Constants import Constants


class Thinker:

    def __init__(self, start_consequence, start_relation):
        self.solutions = []
        self.start_consequence = start_consequence
        self.start_relation = start_relation

    # c - interval [x1, x2]
    def solve_one_inequality(self, y, c):
        res = []
        for elem in c:
            res.append(elem + 1 - y)
        return self.convert_to_correct_form(res)

    def solve_row(self, row, c):
        res = []
        for elem_index in range(len(row)):
            solution = {}
            solution[elem_index] = self.solve_one_inequality(row[elem_index], [c, c])
            for sec_elem_index in range(len(row)):
                if elem_index != sec_elem_index:
                    solution[sec_elem_index] = self.solve_one_inequality(row[sec_elem_index], [c, Constants.INFINITY])
            res.append(solution) if None not in solution.values() else {}
        return res

    def convert_to_correct_form(self, elem):
        if isinstance(elem, list):
            elem = self.convert_list_to_correct_form(elem)
        return elem

    def convert_list_to_correct_form(self, elem):
        if (elem[0] < 0 and elem[1] < 0) or (elem[0]>1 and elem[1]>1):
            return None
        if elem[0] < 0:
            elem[0] = 0
        if elem[1] > 1:
            elem[1] = 1
        return elem

    def solve_rows(self):
        for row_index in range(len(self.start_relation)):
            self.solutions.append(self.solve_row(self.start_consequence[row_index], self.start_relation[row_index][1]))

    def find_interval_intersection(self, interval1, interval2):
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])

        if start <= end:
            return [start, end]
        else:
            return None

    def find_all_intervals(self):
        res = []
        for solution_index in range(len(self.solutions)):
            for sec_solution_index in range(len(self.solutions)):
                if solution_index != sec_solution_index:
                    for item in self.solutions[solution_index]:
                        for sec_item in self.solutions[sec_solution_index]:
                            map = {}
                            for key in item.keys():
                                map[key] = self.find_interval_intersection(item[key], sec_item[key])
                            res.append(map)
        return self.make_unique(res)

    def make_unique(self, li):
        unique_list = []
        for item in li:
            if None not in item.values() and item not in unique_list:
                unique_list.append(item)
        return unique_list
