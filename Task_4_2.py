# Написать два алгоритма нахождения i-го по счёту простого числа. Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена». Примечание ко всему домашнему заданию: Проанализировать скорость
# и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


# простой перебор
def simple_search(n):
    res = [2]
    i = 1
    while len(res) < n:
        i += 2
        j = 3
        while i % j != 0:
            j += 2
        if j == i:
            res.append(j)
    return res


# Решето Эратосфена
def sieve(n):
    a = [i for i in range(n)]
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
        m += 1
    b = [i for i in a if i != 0]
    return b


def main(num):
    result = simple_search(num)
    print(result)
    num = result[-1] + 1
    result2 = sieve(num)
    print(result2)


cProfile.run('main(400)')
cProfile.run('main(4000)')

# 400 простых чисел
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.060    0.060 <string>:1(<module>)
#      1    0.002    0.002    0.003    0.003 Task_4_2.py:23(sieve)
#      1    0.000    0.000    0.000    0.000 Task_4_2.py:24(<listcomp>)
#      1    0.000    0.000    0.000    0.000 Task_4_2.py:34(<listcomp>)
#      1    0.000    0.000    0.060    0.060 Task_4_2.py:38(main)
#      1    0.045    0.045    0.046    0.046 Task_4_2.py:9(simple_search)
#      1    0.000    0.000    0.060    0.060 {built-in method builtins.exec}
#   1371    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.012    0.006    0.012    0.006 {built-in method builtins.print}
#    399    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#  4000 простых чисел
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    5.095    5.095 <string>:1(<module>)
#      1    0.032    0.032    0.036    0.036 Task_4_2.py:23(sieve)
#      1    0.003    0.003    0.003    0.003 Task_4_2.py:24(<listcomp>)
#      1    0.002    0.002    0.002    0.002 Task_4_2.py:34(<listcomp>)
#      1    0.000    0.000    5.095    5.095 Task_4_2.py:38(main)
#      1    5.032    5.032    5.037    5.037 Task_4_2.py:9(simple_search)
#      1    0.000    0.000    5.095    5.095 {built-in method builtins.exec}
#  18907    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#      2    0.022    0.011    0.022    0.011 {built-in method builtins.print}
#   3999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
