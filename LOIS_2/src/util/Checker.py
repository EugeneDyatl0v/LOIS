import json
from re import fullmatch


#надо поменять проверку ввода

class Checker:
    @staticmethod
    def check_interval(x):
        return 0 <= x <= 1

    @staticmethod
    def check_input(start_consequence, start_relation):
        consequence = start_consequence.replace(" ", "").rstrip()
        if fullmatch(r'\w{1}\d{1}:(0.\d+|0|1)(,\w{1}\d{1}:(0.\d+|0|1))*', consequence):
            pass
        else:
            print(f"Неправильный формат ввода следствия. Вывод невозможен.")
        relation = start_relation.replace(" ", "").rstrip()
        try:
            relation = json.loads(relation)
        except:
            print(f"Неправильный формат ввода отношения. Вывод невозможен.")

        consequence = Checker.consequence_to_variables(consequence)
        if len(consequence) != len(relation):
            print("Невозможно построить матрицу. Вывод невозможен.")

        return relation, consequence

    @staticmethod
    def consequence_to_variables(c):
        result = []
        lines = c.split(",")
        for line in lines:
            result.append(tuple([line.split(":")[0], float(line.split(":")[1])]))
        return result

