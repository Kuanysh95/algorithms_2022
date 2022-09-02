"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат. 

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


сompany_revenue = {
    'activision': 8100000,
    'netease': 9600000,
    'nintendo': 8080000,
    'microsoft': 1290000,
    'google': 11000000,
    'apple': 15300000,
    'tencent': 32200000,
    'sony': 18200000,
}


# Первый вариант - O(n log n)
def sorted_1(сompany_revenue):
    company = сompany_revenue.items()
    company = sorted(company, key=lambda x: x[1])
    print(company[-1], company[-2], company[-3])


# Второй вариант - O(n)
def sorted_2(сompany_revenue):
    input_max = {}
    list_d = dict(сompany_revenue)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    print(input_max)


sorted_1(сompany_revenue)
sorted_2(сompany_revenue)

"""
Второй вариант эффективнее, 
так как имеет линейную сложность и решает задачу без лишней сортировки
"""