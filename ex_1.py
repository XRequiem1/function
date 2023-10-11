#високосный год
#def is_year_leap(year):
#    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#        return 'true'
#    else:
#        return 'false'
#print(is_year_leap(int(input('Введите год'))))

#квадрат


#времена года
#def season(a):
#    if a == 1 or a == 2 or a == 3:
#        return 'winter'
#    elif a == 4 or a == 5 or a == 6:
#        return 'spring'
#    elif a == 7 or a == 8 or a == 9:
#        return 'summer'
#    elif a == 10 or a == 11 or a == 12:
#        return 'autumn'
#print(season(int(input("Введите число"))))



#банковский вклад
#def bank(a,years):
#    for i in range(years):
#        a = (a * 1.1)
#        return a
#a = int(input('вклад'))
#years = int(input('год'))
#print(bank(a, years))

#простые числа


#правильная дата
#def date(d,m,y):
#    if d <= 31 and m <= 12 and y <= 2100:
#        return 'True'
#    else:
#        return 'False'
#print(date(int(input('введите день')), int(input('месяц')), int(input('год'))))


#длина отрезка
#def distance(*args):
#    print(args)
#    x1 = args[0]
#    y1 = args[1]
#    x2 = args[2]
#    y2 = args[3]
#    dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#    return dst


#res = distance((int(input)), (int(input)), (int(input)), (int(input)))
#print(res)

# Отрицательная степень
#def power(a, n):
#    res = 1
#    for i in range(abs(n)):
#        res *= a
#    if n >= 0:
#        return res
#    else:
#        return 1 / res
#print(power(float(input()), int(input())))

#числа фибоначи
#def fib(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)
#print(fib(int(input())))

#Посчитать количество одинаковых элементов в списке
#def fill_list(m1, m2, amount, l):
#    from random import randint
#    for i in range(amount):
#        l.append(randint(m1, m2))
#def analysis(your_list, your_dict):
#    for i in your_list:
#        if i in your_dict:
#            your_dict[i] += 1
#        else:
#            your_dict[i] = 1
#lst = []
#dct = {}
#mn = int(input('Минимум: '))
#mx = int(input('Максимум: '))
#qty = int(input('Количество элементов: '))
#fill_list(mn, mx, qty, lst)
#analysis(lst, dct)
#for item in sorted(dct):
#    print("'%d':%d" % (item, dct[item]))

#Циклический сдвиг
#def shift(lst, steps):
#    if steps < 0:
#        steps = abs(steps)
#        for i in range(steps):
#            lst.append(lst.pop(0))
#    else:
#        for i in range(steps):
#            lst.insert(0, lst.pop())
#nums = [4, 5, 6, 7, 8, 9, 0]
#print(nums)
#shift(nums, -2)
#print(nums)
#shift(nums, 3)
#print(nums)


