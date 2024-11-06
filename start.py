# -*- coding: gbk -*-
import random

# ����ÿ��س�ı�ʾ����
SHAOYANG = '1'
SHAOYIN = '0'
LAOYANG = '1*'
LAOYIN = '0*'


# ģ����ͭǮ
def toss_coins():
    # ģ����öͭǮ�Ľ����0�����֣�1����
    coins = [random.randint(0, 1) for _ in range(3)]
    return coins


# ����ͭǮ�������س
def generate_yao(coins):
    count_heads = coins.count(1)
    if count_heads == 1:
        return SHAOYANG
    elif count_heads == 2:
        return SHAOYIN
    elif count_heads == 3:
        return LAOYANG
    elif count_heads == 0:
        return LAOYIN


# ��������
def generate_hexagram():
    hexagram = []
    for _ in range(6):
        coins = toss_coins()
        yao = generate_yao(coins)
        hexagram.append(yao)
    return hexagram


# ����
def regenerate_hexagram(hexagram):
    n_hexagram = []
    for yao in hexagram:
        if yao == LAOYANG:
            n_hexagram.append(SHAOYANG)
        elif yao == LAOYIN:
            n_hexagram.append(SHAOYIN)
        else:
            n_hexagram.append(yao)
    return n_hexagram


# ���ɱ���
def generate_changing_hexagram(hexagram):
    changing_hexagram = []
    for yao in hexagram:
        if yao == LAOYANG:
            changing_hexagram.append(SHAOYIN)
        elif yao == LAOYIN:
            changing_hexagram.append(SHAOYANG)
        else:
            changing_hexagram.append(yao)
    return changing_hexagram


# ��������
def print_hexagram(hexagram):
    line = ""
    for yao in reversed(hexagram):
        line += yao
    return line.rstrip()


# ������
hexagram = generate_hexagram()
n_hexagram = regenerate_hexagram(hexagram)
bengua = print_hexagram(n_hexagram)

shifoubiangua = 0
if any(yao in [LAOYANG, LAOYIN] for yao in hexagram):
    shifoubiangua = 1
    changing_hexagram = generate_changing_hexagram(hexagram)
    biangua = print_hexagram(changing_hexagram)
