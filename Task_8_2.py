# Закодируйте любую строку из трех слов по алгоритму Хаффмана.
# источник https://practice.keyfire.ru/blog/kak-zakodirovat-stroku-s-pomoshyu-algoritma-haffmana/

import heapq
from collections import Counter
from collections import namedtuple


# класс для ветвей дерева - внутренних узлов; у них есть потомки
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# класс для листьев дерева, у него нет потомков, но есть значение символа
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


# функция кодирования строки в коды Хаффмана
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


# функция декодирования исходной строки по кодам Хаффмана
def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


s_in = input('Введите строку ')
d_code = huffman_encode(s_in)
s_encoded = "".join(d_code[ch] for ch in s_in)
s_decode = huffman_decode(s_encoded, d_code)
print('закодированная строка ', s_encoded)
print('раскодированная строка', s_decode)
