import pprint

from src.fun.Thinker import Thinker
from src.util.Checker import Checker
from src.util.FileReader import FileWorker
from src.util.PrettyWriter import PrettyWriter


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
    while True:
        try:
            choice = int(input("Выберите номер следствия и отношения для нахождения обратного нечёткого логического вывода\n"))
            start_consequence, start_relation = FileWorker.read(choice)
            start_consequence, start_relation = Checker.check_input(start_consequence, start_relation)
            thinker = Thinker(start_consequence, start_relation)
            thinker.solve_rows()
            li = thinker.find_all_intervals()
            PrettyWriter.print(li)  # возвращает интервалы значений когда все выполняется
        except Exception as e:
            print(f'{e}')




