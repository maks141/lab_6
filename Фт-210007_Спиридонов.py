import numpy as np
import functools

while True:
    criterion_amount = int(input('Введите количество критериев(начиная от 2): '))
    if criterion_amount < 2:
        print('Введите корректное количество!')
        continue
    else:
        break

crit_name_list = []
for i in range(criterion_amount):
    criterion_name = input('Введите название криетерия №{}: '.format(i + 1))
    crit_name_list.append(criterion_name)

crit_name_list_copy = crit_name_list

# Создаем матрицу (диагональ - единицы)
a = np.eye(criterion_amount)

# Запрос критериев и рассчет обратных значений
while True:
    for i in range(len(crit_name_list)):
        for m in range(len(crit_name_list_copy)):
            if i >= m:
                continue
            else:
                while True:
                    crit = float(input('Введите криетерий попарного сравнения {}/{}: '.format(crit_name_list[i], crit_name_list[m])))
                    if crit < 0:
                        print('Введите корректное значение!')
                        continue
                    else:
                        break
                a[i, m] = round(crit, 2)
                a[m, i] = round(1 / crit, 2)

    lamd = []

    degr_crit = 1 / criterion_amount 
    for i in range(criterion_amount):
        lamd.append(round(functools.reduce(lambda a, b : a * b, a[i]) ** degr_crit, 2))

    s_lamd = sum(lamd)
    correct_kf = []
    kf = {}
    for i in range(len(lamd)):
        kf[crit_name_list[i]] = round(lamd[i] / s_lamd, 2)
        correct_kf.append(round(lamd[i] / s_lamd, 2))

    # Проверка на сумму весовых кф с последующим выводом
    if sum(correct_kf) == 1:
        print('Введенные значения корректны')
        for i in kf:
            print(i + ':', str(kf[i]))
    else:
        print('Сумма весовых коэфицентов не равна единице, введите критерии попарного сравнения заного')
        continue
    break