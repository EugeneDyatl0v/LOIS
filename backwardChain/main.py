#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#// ������������ ������ �1 �� ���������� �2�������� ������ ���������������� ������
#// ������� 6. �������� ���������� max(min(a,b))
#// ��������� ���������� ������ 121701 ����� ����������, ���������, �������, ���������, ������������ 
#// ��������� ��������� �������� �������� �����.
#// 03.12.2023 
#//
#// ��������: ~

import parse, backwardChain as bk


facts, rules = parse.parse()

for el_i, el in enumerate(rules): 
    for item_i, item in enumerate(el[1]):
        rules[el_i][1][item_i] = [item[0],item[2]]

for rule in rules:
    rule = bk.column(rule[1])
    for fact in facts:
        fact = fact[1]
        bk.get_log(rule, fact)