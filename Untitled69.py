#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1

l1 = ['1', '123', '123', '12', '1', '123']
l2 = [len(x) for x in l1]
print(l2)


# In[8]:


#2

l1 = ['1', '123', '123', '12', '1', '123']
count = sum(1 for x in l1 if len(x) > 2)
print(count)


# In[17]:


#3


d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
result = sum(key * value for key, value in d4.items())
print(result)


# In[26]:


#4

d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
d7 = {key: value for key,value in d6.items() if key not in d5}
print(d7)


# In[28]:


#5

l2 = [2, 4, -2, -3, 0 , 11 , 3  ,-1]
new_list = [num * index if index != 0 else num for index, num in enumerate(l2)]
print(new_list)


# In[29]:


#6

l2 = [2, 4, -2, -3, 0 , 11 , 3  ,-1]
new_list = [num for num in l2 if num >= 0]
print(new_list)


# In[34]:


#7

l2 = [2, 4, -2, -3, 0 , 11 , 3  ,-1]
l3 = [i if i >= 0 else l2.index(i) for i in l2]
print(l3)


# In[52]:


#8


def multiply(num1, num2):
    """
    Функция для умножения двух чисел
    """
    return num1 * num2

# Пример использования:
result = multiply(5, 3)
print(result)  

result = multiply(2.5, 4)
print(result) 

result = multiply(7.5, 8)
print(result)

result = multiply(1.6, 9)
print(result)


# In[55]:


#9

def multiply(*args):
    """
    Функция для умножения от одного до трех чисел
    """
    result = 1
    for num in args:
        result *= num
    return result

# Пример использования:

result = multiply(4, 2, 3)
print(result) 

result = multiply(7, 9, 23)
print(result)

result = multiply(11, 34, 1)
print(result)


# In[82]:


#10 отвечаем

def multiply(*args):  #исп-ую функцию multiply, которая использует args в качестве параметра, чтобы позволить передать переменное количество аргументов в функцию. Внутри функции происходит умножение всех переданных 
    
    result = 1
    for num in args:
        result *= num   #вызываю функцию multiply с этими переменными как аргументами, используя звездочку  перед каждой переменной, чтобы распаковать значения из кортежей и передать их в качестве отдельных аргументов функции.
    return result

a1 = (15, 10, 5)
result1 = multiply(*a1)
print(result1) 

a2 = (3, 1)
result2 = multiply(*a2)
print(result2)  

a3 = [2, 35, 55]
result3 = multiply(*a3)
print(result3)

a4 = (5, 10, 15)
result4 = multiply(*a4)
print(result4)  

a5 = (10 ,15, 20)
result5 = multiply(*a5)
print(result5)


# In[105]:


#11 отвечаем


def multiply(*args):
    
    result = 1
    for num in args:
        result *= num
    return result


a1 = (15, 10, 5)
result1 = multiply(*a1)
print(result1)  

a2 = (3, 1)
result2 = multiply(*a2)
print(result2)  

a3 = [2, 35, 55]
result3 = multiply(*a3)
print(result3)  

a4 = (5, 10, 15, 20, 23)
result4 = multiply(5, 10, 15, 20)
print(result4)  


# In[86]:


#12


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x // y  # Целочисленное деление
    else:
        return "Ошибка: деление на ноль"

# Запрашиваем у пользователя два целых числа и желаемую операцию
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
operation = input("Выберите операцию (+, -, *, /): ")

# Выполняем выбранную операцию и выводим результат
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Ошибка: неправильная операция"

print("Результат операции:", result)


# In[88]:


#13


def calc(expression):
    # Разбиваем входную строку на отдельные компоненты
    components = expression.split()
    num1 = int(components[0])
    operator = components[1]
    num2 = int(components[2])

    # Выполняем заданную арифметическую операцию
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 // num2  # Целочисленное деление
        else:
            return "Ошибка: деление на ноль"
    elif operator == '%':
        return num1 % num2
    elif operator == '^':
        return num1 ** num2
    else:
        return "Ошибка: неправильная операция"

result = calc('29 - 16')
print(result)  


# In[89]:


#14


def print_car_info(**kwargs):
    car_info = {
        'марка': kwargs.get('марка', 'Неизвестно'),
        'модель': kwargs.get('модель', 'Неизвестно'),
        'цвет': kwargs.get('цвет', 'Неизвестно'),
        'год': kwargs.get('год', 'Неизвестно'),
        'пробег': kwargs.get('пробег', 'Неизвестно'),
        'номер': kwargs.get('номер', 'Неизвестно'),
        'цена': kwargs.get('цена', 'Неизвестно')
    }
    message = f"Автомобиль марки: {car_info['марка']}, модели: {car_info['модель']}, цвета: {car_info['цвет']}, {car_info['год']} года выпуска, с пробегом: {car_info['пробег']} км, с номерным знаком: {car_info['номер']}, цена: {car_info['цена']} руб."
    print(message)

c1 = {
    'марка': 'BMW',
    'модель': 'X5',
    'цвет': 'белый',
    'год': 2006,
    'пробег': '215 000',
    'номер': 'X012AM77',
    'цена': '1 115 000'
}

c2 = {
    'марка': 'Toyota',
    'модель': 'RAV4',
    'год': 2015,
    'пробег': '85 000',
    'цена': '950 000'
}

print_car_info(**c1)
print_car_info(**c2)


# In[106]:


def to_text(number):
    units = ('', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')
    tens = ('', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто')
    teens = ('десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать')

    if number == 0:
        return 'Ноль'
    elif number < 10:
        return units[number]
    elif number < 20:
        return teens[number - 10]
    else:
        unit = number % 10
        ten = number // 10
        return f'{tens[ten]} {units[unit]}'

# Пример использования
print(to_text(13))  


# In[94]:


def to_int(text):
    units = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9}
    tens = {'десять': 10, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90}
    teens = {'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19}

    words = text.split()
    number = 0
    i = 0
    while i < len(words):
        if words[i] in units:
            number += units[words[i]]
        elif words[i] in tens:
            number += tens[words[i]]
        elif words[i] in teens:
            number += teens[words[i]]
        elif words[i] == 'сто':
            number += 100
        elif words[i] == 'двести':
            number += 200
        elif words[i] == 'триста':
            number += 300
        i += 1
    return number

# Пример использования функции
print(to_int('десять')) 


# In[100]:


def calc(expression):
    words = expression.split()
    num1 = to_int(words[0])
    num2 = to_int(words[2])
    operation = words[1]
    
    if operation == 'плюс':
        result = num1 + num2
    elif operation == 'минус':
        result = num1 - num2
    elif operation == 'умножить':
        result = num1 * num2
    
    return(result)

# Пример использования функции
print(calc('семь плюс три')) 


# In[ ]:





# In[ ]:




