# Лабораторная работа по ЛОИС №1.
#
# Вариант: B
#
# Автор: Дятлов Е.А.
#        Олешкевич А.С.
#        Простас А.А.
#
# Номер группы: 121701
#
# Источники: 1.	Ivashenko, V. Application of an integration platform for ontological model-based problem solving
#               using an uniﬁed semantic knowledge representation / V. Ivashenko //
#               Открытые семантические технологии проектирования интеллектуальных систем =
#               Open Semantic Technologies for Intelligent Systems (OSTIS-2021) : сборник научных трудов
#               Белорусский государственный университет информатики и радиоэлектроники;
#               редкол.: В. В. Голенков [и др.]. – Минск, 2021. – Вып. 5. – С.179–186.
#
#            2. Интеграционная платформа

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from gen.unclear_coverageLexer import unclear_coverageLexer
from gen.unclear_coverageParser import unclear_coverageParser
from src.ParseFile import ParseFile
from src.UnclearCoverageMaker import UnclearCoverageMaker, TUPLEException


class FORMULAException(RuntimeError):
    pass


class ExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise FORMULAException(f"{line}:{column}: {msg}")


def check_formula(formula: str):
    data = InputStream(formula)
    lexer = unclear_coverageLexer(data)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ExceptionErrorListener())
    stream = CommonTokenStream(lexer)
    parser = unclear_coverageParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ExceptionErrorListener())
    parser.formula()


def checking_formula(inp):
    try:
        check_formula(inp)
    except FORMULAException as e:
        print(f'Это не формула {e}')


def check_file():
    tests = open('tests.txt', 'r').read().split('\n')
    for test in tests:
        print(test)
        checking_formula(test)


def check_mode():
    flag = ""
    while flag != "n" and flag != "no":
        formula_1 = input("Введите первую формулу\n")
        formula_2 = input("Введите вторую формулу\n")
        premise = input("Введите посылку\n")
        try:
            check_formula(formula_1)
            check_formula(formula_2)
            unclear_coverage_maker = UnclearCoverageMaker(formula_1, formula_2, premise)
            set_1 = unclear_coverage_maker.conclusion()
            print(set_1)
            flag = input("желаете продолжить? (y/n) \n")
        except FORMULAException as e:
            print(f"Это не формула: {e}")
        except TUPLEException as e:
            print(f'{e}')


def checking_file():
    data = ParseFile.parse_file('D:\\LOIS\\LOIS\\LOIS_1\\input')
    for rule in data['rules']:
        for pr in data['facts']:
            set1 = data['facts'][rule[0]]
            set2 = data['facts'][rule[1]]
            premise = data['facts'][pr]
            try:
                check_formula(set1)
                check_formula(set2)
                checking_formula(premise)
                unclear_coverage_maker = UnclearCoverageMaker(set1, set2, premise)
                res = unclear_coverage_maker.conclusion()
                print(f"{set1}\t->\t{set2}")
                print(f"Premise: {premise}")
                print(res)
                print()
            except FORMULAException as e:
                print(f"Это не формула: {e}")
            except TUPLEException as e:
                print(f'{e}')



if __name__ == '__main__':
    while True:
        choice = input('Меню\n1-Проверить формулу, введённую вручную\n2-Проверить формулы из файла\n3-Прямой нечёткий логический вывод, используя импликацию Гогена\n4-проверить вывод из файла\n5-Выход\n')
        if choice == '1':
            checking_formula(input('Формула: '))
        elif choice == '2':
            check_file()
        elif choice == '3':
            check_mode()
        elif choice == '4':
            checking_file()
        elif choice == '5':
            break
