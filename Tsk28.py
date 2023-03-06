# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def sum_number(number_one, number_two):
    if number_two == 0:
        return number_one
    return sum_number(number_one+1, number_two-1)


print(sum_number(15, 1))
