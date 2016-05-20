#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import date, datetime


def getsystime():
    today = list()
    for n in str(date.today()).split('-'):
        today.append(int(n))
    weekday = date(*tuple(today)).weekday()
    hour = datetime.now().hour
    return weekday, hour

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
    total = total * 0.95 if count >= 10 else total
    
    return total

if __name__ == '__main__':
    adult = int(input('請輸入大人人數：'))
    child = int(input('請輸入小孩人數：'))
    weekday, hour = getsystime()
    t = 'special' if weekday > 4 or (hour > 17 and hour < 24) else 'regular'
    print(t)
    print('總價為：%d' % ticket([adult, child], t))

