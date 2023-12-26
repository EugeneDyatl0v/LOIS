answers = [
    {0: [0.9, 0.9], 1: [0.9, 0.9], 2: [0.6, 1]},
    {0: [0.9, 0.9], 1: [0.9, 0.9], 2: [0.6, 0.6]},
    {0: [0.9, 1], 1: [0.9, 0.9], 2: [0.6, 0.6]}
]


def is_interval_inside(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    return start2 <= start1 and end1 <= end2


def remove_nested_answers(answers):
    remaining_answers = []

    for i, answer in enumerate(answers):
        is_nested = False

        for j, other_answer in enumerate(answers):
            if i != j:  # Исключаем сравнение ответа с самим собой
                intervals_match = True

                for key, interval in answer.items():
                    if key in other_answer:
                        if not is_interval_inside(interval, other_answer[key]):
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


filtered_answers = remove_nested_answers(answers)
print(filtered_answers)