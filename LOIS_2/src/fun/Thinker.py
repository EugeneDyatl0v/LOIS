import itertools

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
            res.append(round(elem + 1 - y, 4))
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

        if len(res) == 0:
            raise Exception('Нет решений')
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

    def find_intersection(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if interval[0] <= result[1]:
                result = [max(interval[0], result[0]), min(interval[1], result[1])]
            else:
                return None

        if result[0] <= result[1]:
            return result
        else:
            return None

    def find_all_intervals(self):
        res = []
        combinations = list(itertools.product(*self.solutions))
        for combination in combinations:
            map = {}
            for key in combination[0].keys():
                elements = [item[key] for item in combination]
                map[key] = self.find_intersection(elements)
            if None not in map.values():
                res.append(map)
        unique_res = self.make_unique(res)
        return self.remove_nested_answers(unique_res)

    def make_unique(self, li):
        unique_list = []
        for item in li:
            if None not in item.values() and item not in unique_list:
                unique_list.append(item)
        return unique_list

    def is_interval_inside(self, interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        return start2 <= start1 and end1 <= end2

    def remove_nested_answers(self, answers):
        remaining_answers = []

        for i, answer in enumerate(answers):
            is_nested = False

            for j, other_answer in enumerate(answers):
                if i != j:  # Исключаем сравнение ответа с самим собой
                    intervals_match = True

                    for key, interval in answer.items():
                        if key in other_answer:
                            if not self.is_interval_inside(interval, other_answer[key]):
                                intervals_match = False
                                break
                        else:
                            intervals_match = False
                            break

                    if intervals_match:
                        is_nested = True
                        break

            if not is_nested:
                remaining_answers.append(answer)

        return remaining_answers
