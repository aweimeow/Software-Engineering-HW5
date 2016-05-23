#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


def ticket(l, t):
    cost = {'regular': [268, 120], 'special': [368, 150]}
    adult, child = l[:]
    count = adult + child
    if adult + child > 3:
        for i in range((adult + child)//3):
            if child > 0:
                child = child - 1
            else:
                adult = adult - 1
    f = lambda x: x[0] * x[1]
    total = sum(map(f, zip(cost[t], [adult, child])))
    total = total * 1.1 if t == 'special' else total
    total = total * 0.95 if count >= 10 else total
    
    return total

if __name__ == '__main__':
    try:
        t = int(input('請輸入時間（平日中午 1、平日晚上 2、假日 3）: '))
        if t > 3 or t < 1:
            sys.exit()
    except:
        print('輸入錯誤'); sys.exit()
    adult = int(input('請輸入大人人數：'))
    child = int(input('請輸入小孩人數：'))
    t = 'regular' if t == 1 else 'special'
    print('總價為：%d' % ticket([adult, child], t))

