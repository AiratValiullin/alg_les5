# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict
f = 0
e = 0
comp = int(input('Введите количество предприятий: '))
my_dict = defaultdict(list)

for i in range(comp):
    my_list = []
    c = 0
    a = input('Название компании: ')

    for j in range(4):
        b = int(input(f'Прибыль за {j+1} квартал: '))
        my_list.append(int(b))

    for k in my_list:
        c += int(k)
    d = int(c / 4)
    my_dict[str(a)].append(int(d))

    print(f'Средняя прибыль компании {comp} за год - {d} ')

for l, n in my_dict.items():
    e += n[0]
e = int(e / comp)

for z, x in my_dict.items():
    if x[0] >= e:
        print(f'Прибыль компании {z} выше средней')
    else:
        print(f'Прибыль компании {z} ниже средней')








