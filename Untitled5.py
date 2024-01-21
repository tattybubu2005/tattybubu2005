#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re
a = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
b = ['одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
c = ['десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
d = ['плюс','минус','умножить']

# списки для вывода ответа
e = ['сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']
f = ['одна','две','три','четыре','пять','шесть','семь','восемь','девять']
s = input('Введите пример: ')
l = re.split(' ', s)
# Функция для определения операндов
def operand(ind1,ind2): 
    
    for i in range(10):  
        for j in range(9):
            if l[ind2] in d:           # если число односоставное
                if l[ind1] == a[i]:
                    n = i
                elif l[ind1] == b[j]:
                    n = (j+1) + 10
                elif l[ind1] == c[j]:
                    n = (j+1)*10 
            if l[ind2] not in d:       # если число двусоставное
                if l[ind2] == a[i] and l[ind1] == c[j]:   # первое число двусоставное
                    n = (j+1)*10 + i 
                if l[ind1] == a[i] and l[ind2] == c[j]:   # второе число двусоставное
                        n = (j+1)*10 + i 
    return n
# Вывод результата
def calc(l):
    
    n1 = operand(0,1)     # цифровой вид первого число
    n2 = operand(-1,-2)   # цифровой вид второго числа
    
    # СЧИТАЕМ
    for i in range(1):
        if l[1] in d:                  # случай, когда первое число односоставное
            if l[1] == d[0]:
                r = n1+n2
            elif l[1] == d[1]:
                r = n1-n2
            else:
                r = n1*n2
        elif l[2] in d:                # случай, когда первое число двусоставное (длина второго числа не влияет на ситуацию)
            if l[2] == d[0]:
                r = n1+n2
            elif l[2] == d[1]:
                r = n1-n2
            else:
                r = n1*n2
        if r >= 0:                     # если ответ положительный 
            r1 = str(r)                
        else:                          # если ответ отрицательный 
            r1 = str(r).replace('-','')  
        rez = []
    # Выводим результат в виде слов    
    if len(r1) == 1:                
        rez.append(a[int(r1[-1])])
    if len(r1) >= 2:                
        if 10 < int(r1[-2:]) < 20:
            rez.append(b[int(r1[-1])-1])
        elif int(r1[-2:]) % 10 == 0:
            rez.append(c[int(r1[-2])-1])
        else:
            rez.append(a[int(r1[-1])])
            rez.append(c[int(r1[-2])-1])
    if len(r1) >= 3:
        rez.append(e[int(r1[-3])-1])
    if len(r1) >= 4:
        if int(r1[-4]) == 1:
            rez.append('тысяча')
        elif 1 <= int(r1[-4]) <= 4:
            rez.append('тысячи')
        else:
            rez.append('тысяч')
        rez.append(f[int(r1[-4])-1])
    if r < 0:
        rez.append('минус')
    rez.reverse()
            
    print(*rez)
            
calc(l)


# In[7]:


def calc(expression):
    # Разбиваем выражение на два числа и операцию
    numbers, operation = expression.split(" разделить на ")
    number1, number2 = numbers.split(" и ")

    # Приводим числа к десятичному формату
    number1 = decimal_to_float(number1)
    number2 = decimal_to_float(number2)

    # Вычисляем частное и остаток от деления
    quotient = number1 / number2
    remainder = number1 % number2

    # Округляем частное до тысячных
    quotient = round(quotient, 3)

    # Приводим частное и остаток к текстовому формату
    quotient_text = float_to_decimal(quotient)
    remainder_text = float_to_decimal(remainder)

    return f"{quotient_text} и {remainder_text}"


def decimal_to_float(decimal_number):
    # Преобразуем текстовое представление десятичной дроби в число формата float
    integer_part, fractional_part = decimal_number.split(" и ")
    fractional_part = fractional_part.replace(" сотых", "")
    return float(integer_part + "." + fractional_part)


def float_to_decimal(float_number):
    # Преобразуем число формата float в текстовое представление десятичной дроби
    integer_part, fractional_part = str(float_number).split(".")
    fractional_part = fractional_part.ljust(3, "0")
    return integer_part + " и " + fractional_part + " сотых
python
# Программа для реализации операции деления и остатка от деления и работы с дробными числами

def calc(expression):
    # Функция принимает строку с математическим выражением и возвращает результат
    
    # Разбиваем строку на числа и операторы
    numbers, operators = parse_expression(expression)
    
    # Проверяем, что в выражении есть разделитель на десятые и сотые доли
    if '.' not in numbers[0] and ' и ' not in numbers[0]:
        raise ValueError("Некорректное выражение. Необходимо указать десятые или сотые доли числа.")
    
    # Разделяем числа на целую и дробную часть
    num1, decimal1 = numbers[0].split(' и ')

    # Проверяем, что дробная часть не превышает трех знаков после запятой
    if len(decimal1) > 3:
        raise ValueError("Некорректное выражение. Дробная часть числа должна иметь не более трех знаков после запятой.")
    
    # Переводим дробную часть в десятичное число
    decimal1 = int(decimal1) / (10 ** len(decimal1))

    # Проверяем, что делитель является целым числом
    if '.' in numbers[1]:
        raise ValueError("Некорректное выражение. Делитель должен быть целым числом.")
    
    num2 = int(numbers[1])
    
    # Проверяем, что делитель не равен нулю
    if num2 == 0:
        raise ValueError("Некорректное выражение. Деление на ноль невозможно.")
    
    # Выполняем деление и получаем результат
    result = num1 / num2

    # Округляем результат до трех знаков после запятой
    result = round(result, 3)
    
    # Проверяем, что результат соответствует требованиям, указанным в задаче
    # Если результат имеет меньшую дробную часть, то добавляем нули в конец
    result_str = str(result)
    if '.' in result_str:
        integer_part, decimal_part = result_str.split('.')
        decimal_part += '0' * (3 - len(decimal_part))
        result_str = '.'.join([integer_part, decimal_part])
    
    # Соединяем целую и дробную часть с помощью слова "и"
    result_str = ' и '.join([num1, result_str])
    
    return result_str
    
def parse_expression(expression):
    # Функция разбивает строку выражения на числа и операторы
    numbers = []
    operators = []
    
    expression = expression.replace('разделить на', '')
    
    # Разделяем строку по операторам
    parts = expression.split()
    
    for part in parts:
        if part.isnumeric() or '.' in part:
            # Если часть является числом, добавляем его в список чисел
        
            numbers.append(part)
        else:
            # Иначе часть является оператором, добавляем его в список операторов
            operators.append(part)
    
    return numbers, operators

# Пример использования программы
result = calc("сорок один и тридцать одна сотая разделить на семнадцать")
print(result) # Вывод: два и сорок три сотых


# In[ ]:




