class FileWorker:

    @staticmethod
    def read(count):
        count -= 1
        with open("input", 'r') as file:
            lines = file.readlines()
        if len(lines) >= count * 3 + 2 and count >= 0:
            consequence = lines[count * 3]
            relation = lines[count * 3 + 1]
            return consequence, relation
        else:
            if count != -2:
                raise Exception("Неверный номер следствия")
            else:
                raise Exception("Выход из программы")

    @staticmethod
    def write(consequence, relation, result):
        with open("output", 'r') as file:
            lines = file.readlines()
        answer = f"Для следствия {consequence} и отношения {relation} обратный нечёткий логический вывод: {result}\n"
        with open("output", 'a') as file:
            for line in lines:
                if line == answer:
                    return
            file.write(answer)
