# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания
# первых трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile


# вариант с переменными
def multiple_var(a1, a2, b1, b2):
    for i in range(b1, b2):
        cnt = 0
        for n in range(a1, a2):
            if n % i == 0:
                cnt += 1
        print(f'на {i} делится {cnt} чисел')
    print()


# вариант со списками
def multiple_list(a1, a2, b1, b2):
    for i in range(b1, b2):
        b = [n for n in range(a1, a2) if n % i == 0]
        print(f'на {i} делится {len(b)} чисел из заданного диапазона')
    print()


# вариант со словарем
def multiple_dict(a1, a2, b1, b2):
    d = {}
    for key in range(b1, b2):
        val = d.setdefault(key, 0)
        for n in range(a1, a2):
            if n % key == 0:
                val += 1
        d[key] = val
    for key, val in d.items():
        print(f'на {key} делится {val} чисел')


def multiple(a_1, a_2, b_1, b_2):
    multiple_var(a_1, a_2, b_1, b_2)
    multiple_list(a_1, a_2, b_1, b_2)
    multiple_dict(a_1, a_2, b_1, b_2)


cProfile.run('multiple(2, 100, 2, 100)')
cProfile.run('multiple(2, 1000, 2, 100)')
cProfile.run('multiple(2, 10000, 2, 100)')

# 100 чисел
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.023    0.023 <string>:1(<module>)
#      1    0.001    0.001    0.014    0.014 Task_4_1.py:19(multiple_list)
#     98    0.001    0.000    0.001    0.000 Task_4_1.py:21(<listcomp>)
#      1    0.002    0.002    0.003    0.003 Task_4_1.py:27(multiple_dict)
#      1    0.000    0.000    0.023    0.023 Task_4_1.py:39(multiple)
#      1    0.002    0.002    0.005    0.005 Task_4_1.py:8(multiple_var)
#      1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#     98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    296    0.017    0.000    0.017    0.000 {built-in method builtins.print}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#     98    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}

# 1000 чисел
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.068    0.068 <string>:1(<module>)
#      1    0.001    0.001    0.034    0.034 Task_4_1.py:19(multiple_list)
#     98    0.015    0.000    0.015    0.000 Task_4_1.py:21(<listcomp>)
#      1    0.015    0.015    0.017    0.017 Task_4_1.py:27(multiple_dict)
#      1    0.000    0.000    0.068    0.068 Task_4_1.py:39(multiple)
#      1    0.016    0.016    0.018    0.018 Task_4_1.py:8(multiple_var)
#      1    0.000    0.000    0.068    0.068 {built-in method builtins.exec}
#     98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    296    0.021    0.000    0.021    0.000 {built-in method builtins.print}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#     98    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}

# 10000 чисел
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.465    0.465 <string>:1(<module>)
#      1    0.001    0.001    0.097    0.097 Task_4_1.py:19(multiple_list)
#     98    0.093    0.001    0.093    0.001 Task_4_1.py:21(<listcomp>)
#      1    0.152    0.152    0.153    0.153 Task_4_1.py:27(multiple_dict)
#      1    0.000    0.000    0.465    0.465 Task_4_1.py:39(multiple)
#      1    0.211    0.211    0.215    0.215 Task_4_1.py:8(multiple_var)
#      1    0.000    0.000    0.465    0.465 {built-in method builtins.exec}
#     98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    296    0.008    0.000    0.008    0.000 {built-in method builtins.print}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#     98    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
