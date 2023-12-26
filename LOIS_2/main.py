import pprint

from src.fun.Thinker import Thinker
from src.util.Checker import Checker
from src.util.FileReader import FileWorker


def pretty_print(obj, indent=0):
    if isinstance(obj, dict):
        for key, value in obj.items():
            print('\t' * indent + str(key) + ':')
            pretty_print(value, indent + 1)
    elif isinstance(obj, list):
        for item in obj:
            pretty_print(item, indent)
    else:
        print('\t' * indent + str(obj))


if __name__ == '__main__':
    choice = int(input("Выберите номер следствия и отношения для нахождения обратного нечёткого логического вывода\n-1 для выхода \n--->"))
    start_consequence, start_relation = FileWorker.read(choice)
    start_consequence, start_relation = Checker.check_input(start_consequence, start_relation)
    thinker = Thinker(start_consequence, start_relation)
    thinker.solve_rows()
    pprint.pprint(thinker.find_all_intervals()) # возвращает интервалы значений когда все выполняется




