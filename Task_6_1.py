# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.

from memory_profiler import profile


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


@profile
def multiple(a_1, a_2, b_1, b_2):
    multiple_var(a_1, a_2, b_1, b_2)
    multiple_list(a_1, a_2, b_1, b_2)
    multiple_dict(a_1, a_2, b_1, b_2)


multiple(2, 10000, 2, 100)


# версия Python 3.10.1  разрядность ОС 64-bit
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     42     19.2 MiB     19.2 MiB           1   @profile
#     43                                         def multiple(a_1, a_2, b_1, b_2):
#     44     19.3 MiB      0.0 MiB           1       multiple_var(a_1, a_2, b_1, b_2)
#     45     19.6 MiB      0.4 MiB           1       multiple_list(a_1, a_2, b_1, b_2)
#     46     19.6 MiB      0.0 MiB           1       multiple_dict(a_1, a_2, b_1, b_2)
