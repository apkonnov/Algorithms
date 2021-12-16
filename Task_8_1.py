# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

s = input('Введите строку ')
len_s = len(s)
cnt_subs = 0
for len_subs in range(1, len_s):
    lst_subs = [hashlib.sha1(bytes(s[i:i+len_subs].encode('utf-8'))).hexdigest() for i in range(len_s-len_subs+1)]
    cnt_subs += len(set(lst_subs))
print(f'Количество различных подстрок = {cnt_subs}')
