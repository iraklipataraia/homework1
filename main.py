from audioop import reverse
from itertools import count
# from lib2to3.fixes.fix_input import context
from math import sqrt,fmod, factorial
import random
from os import write
from os.path import split
from statistics import median, mode


from numpy.ma.core import append, multiply
from soupsieve.util import lower

# x = 42 + 3 * 3
# y = 2 + 4
# z = x / y
# 
# print(z)
# 
# a = 1
# b = 4
# 
# a , b = b , a
# 
# 
# print(a)
# print(b)
# 
# 
# name = 'Irakli'
# last_name = 'Pataraia'
# 
# print(name,last_name)
# 
# a = 2
# b = 4
# c = 6
# 
# d = a + b + c
# 
# avg = (a + b + c)/ 3
# 
# print(avg)
# 
# celsius = 36
# fahrenheit = (celsius * 9 / 5) + 32
# print(fahrenheit)
# 
# 
# 
# a = (3 + 145) * 4 + 3 ** 2
# b = (2 + 3) ** 5
# print(a / b)
# 
# number_one = 150
# number_two = 40
# 
# number_one, number_two = number_two, number_one
# 
# print(number_one, number_two)
# 

# name = 'Irakli'
# last_name = 'Pataraia'
# age = 33
# print(name,last_name,age,'years old')
#
#
# fahrenheit = 90
# celsius = (fahrenheit - 32) * 5 / 9
# print(celsius)
#


# a = 5
# b = 6
#
# print (a + b)
# print (a - b)
# print (a * b)
# print (a / b)
#
# c = (5*2**7)/(5-1)
# print(c)
#
# first_name = 'Irakli'
# last_name = 'Pataraia'
# print(first_name)
# print(last_name)
#
# degree = 45
# radians = (3.14/180) * degree
# print(radians)
#
# a = 5
# b = 7
# print(a,b)
# a,b = b,a
# print (a,b)
#
# first_name = 'Irakli'
# last_name = 'Pataraia'
# print(first_name,'$', last_name)
#
#
# a = int(input('Number one: '))
# b = int(input('Number two: '))
# c = int(input('Number three: '))
#
# sum = (a + b + c)/3
# print(sum)

# hours_per_day = int(input('amount_of_hour: '))
# salary_per_hour = int(input('salary_per_hour: '))
# monthly_salary = hours_per_day * salary_per_hour * 30
#
# print(monthly_salary)
#
# print( 20 >= 5)
# print(True and not False)
# print(not True and not False)
# print(4 != 4.0)
# print(True or not False)


# birth_year = int(input('enter birth year: '))
# getting_80 = birth_year + 80
# print('you will get 80 in', getting_80 )


# number = int(input('enter your number: '))
# if (number%5==0):
#     print('xutis jeradi')
# else:
#     print('araa xutis jeradi')

# number = int(input('enter your number: '))
# if number > 0:
#     print('number is pisitive')
# elif number < 0:
#     print('number is negative')
# else:
#     print('number is zero')

# number1 = int(input('enter number 1: '))
# number2 = int(input('enter number 2: '))
#
# print(number1 + number2)
#
# birth_year = int(input('enter birth year: '))
# print(2024 - birth_year)


# x = int(input('enter x: '))
# if x > 0:
#     y = (x/5) + (2+x)**3
#     print(y)
# else:
#     y = 5 * x + ((3+x**5)/4)
#     print(y)
#


# n = 10
#
# while n <= 150:
#     n += 5
#     if n ==90:
#         continue
#     print(n)

#
# for i in range(10,150,5):
#     # print (i)
#     if i == 60 or i==75 or i==85:
#         continue
#     print(i)


# x= int(input('enter number: '))
# f = 1
# for i in range(1,x+1):
#     f *= i
# print(f)

# x= int(input('enter number: '))
# f = 1
# start = 1
# while start <= x:
#     f *= start
#     start += 1
# print(f)

# print( pow(4.5,5))








# number = int(input('Enter a number: '))
# if number % 9 == 0:
#     print(number**2)
# else:
#     print(number*2)

# number1 = int(input('Enter number 1: '))
# number2 = int(input('Enter number 2: '))
# if (number1 > 0 and number2 > 0):
#     print(number1 + number2)
# else:
#     print(number1 * number2)

# num_one = int(input('enter num_one: '))
# num_two = int(input('enter num_two: '))
# num_three = int(input('enter num_three: '))
#
# if num_one > num_two and num_one > num_three:
#     print('max number is', num_one)
# elif num_two > num_one and num_two > num_three:
#     print('max number is', num_two)
# else:
#     print('max number is', num_three)


# n = 100
# while n < 490:
#     n += 10
#     if n == 200 or n == 300 or n == 400:
#         continue
#     print(n)

# for i in range(100,500,10):
#     if i == 200 or i == 300 or i == 400:
#         continue
#     print(i)
#
# for i in range(5,20):
#     if i==15:
#          break
#     if i % 2 !=0:
#         print(i)

# for i in range(15,100,5):
#     if i == 45 or i ==55 or i == 65:
#         continue
#     print(i)
# n = 15
# while n < 95:
#     n +=5
#     if n == 45 or n ==55 or n == 65:
#         continue
#     print(n)

# for i in range(20,151):
#     if i%3==0:
#         print(i)
#
# n=20
# while n < 150:
#     n+=1
#     if n%3==0:
#         print(n)

# n = int(input('enter number: '))
# for i in range(1,n):
#    if n % i ==0:
#     print(i)

# n = int(input('enter number: '))
# i=0
# while i <= n:
#     i +=1
#     if i == n:
#         break
#     if n % i ==0:
#         print(i)

# n = int(input('enter number: '))
# f = 1
# for i in range(1, n+1):
#     f *= i
#     print(f)

#
# sum = 0
# for i in range(1,100):
#     if i % 2 != 0:
#         sum += i
# print(sum)

# x = '* '
# y = '*       *'
# i = 0
# while i < 8:
#     if i == 1:
#         print(x * 5)
#     i += 1
#     if i == 2:
#         print (y)
#     if i == 3:
#         print(y)
#     if i == 4:
#         print(x * 5)
#     if i ==5:
#         print(y)
#     if i == 6:
#         print (y)
#     if i == 7:
#         print (x * 5)
#

#

# x = '* '
# i = 0
# while i < 8:
#     if i == 1:
#         print(x * 5)
#     i += 1
#     if i == 2:
#         print (x,'    ',x)
#     if i == 3:
#         print (x,'    ',x)
#     if i == 4:
#         print(x * 5)
#     if i ==5:
#         print (x,'    ',x)
#     if i == 6:
#         print (x,'    ',x)
#     if i == 7:
#         print (x * 5)


# x = int(input('enter your number: '))
# if x > 90 and x <= 100:
#     print('you got A')
# elif x > 80 and x <= 90:
#     print('you got B')
# elif x > 70 and x <= 80:
#     print('you got C')
# elif x > 60 and x <= 70:
#     print('you got D')
# elif x > 50 and x <= 60:
#     print('you got E')
# elif x > 40 and x <= 50:
#     print('you got FX')
# elif x >= 0 and x <= 40:
#     print('you got Failed')


# for i in range(10, 150, 5):
#     if i ==60 or i == 75 or i == 80:
#         continue
#     print(i)
#
# n = 10
# while n < 150:
#     n +=5
#     if n ==60 or n == 75 or n == 80:
#         continue
#     print(n)

# for i in range(20,150):
#     if i%10 ==0:
#         print(i)

# n = 20
# while n < 150:
#     n+=1
#     if n%10==0:
#         print(n)

# x = int(input('enter number: '))
# for i in range(1, x+1):
#    if x % i == 0:
#         print(i)

# x = int(input('enter a number: '))
# f = 1
# for i in range(1,x+1):
#     f *= i
#     print(f)
#
# x = '*'
# while :
#     x += x
#     print(x)

#
# x = 0
# for i in range(1,6):
#     x += 1
#     print("* "* x)
# for i in range(1,6):
#     x -=1
#     print("* "* x)



# number_one = int(input('enter number one: '))
# number_two = int(input('enter number two: '))
# number_three = int(input('enter number three: '))
# print(max(number_one,number_two,number_three))
# print(min(number_one,number_two,number_three))


# x = sqrt(225625)
# y = sqrt(4225)
# print(x,y)

# x = 3**8
# print(x)
# y= 2**9
# print(y)
# z= 10
# print(fmod(y,z))

# number = float(input('enter your number: '))
# print(round(number,2))

# number = int(input('enter your number: '))
# print(factorial(number))
#


# def square(number):
#     number=number ** 2
#     return(number)
#
# print(square(4))


# def print_hello_name(name):
#     print('Hello', name)
#
# print_hello_name("Irakli")

# def avg(num1 = 5,num2 = 1):
#     """
#     This function calculates avg of two number.
#
#     Args:
#
#     num1 is first argument.
#     num2 is second argument.
#
#
#     :return:
#     """
#     return((num1+num2)/2)
#
# x = avg()
# print(x)

# text = 'hello world'
# print(text[:6])

#
# string_1 = input('Enter string1: \n')
# string_2 = input('Enter string2: \n')
#
# if string_1 == string_2:
#     print('strings are equal')
# else:
#     print('not equal')


# text = 'Hello world'
# index = len(text)
# while index >= 0:
#     print(text[index])
#     index -= 1


# text = 'Hello world'
# # for i in text[::-1]:
# #     print(i)
#
# for i in range(len(text)-1,-1,-1):
#     print(text[i])


# text = 'Hello World'
# space_index = 0
# for i in range(len(text)):
#         if text[i] == ' ':
#             space_index = i
#
#         if space_index ==0:
#             print(text[i])
#         else:
#             for j in text[:space_index:-1]:
#                 print(j)
#             break

# greeting = 'Hello'
# print(greeting)
# greeting_new = 'L' + greeting[1:]
# print(greeting_new)

# greeting = 'Hello'
# greeting_new = greeting.replace('H', 'L')
# print(greeting_new)

# name = input('enter your name: ')
# age = int(input('enter your age: '))
#
# if age < 0:
#     print(f'{name} enter correct age!')
# elif age >= 18:
#     print(f'{name} you can take driving license')
# else:
#     print(f'{name} you can not take driving license!')

#
# for i in range(10,101):
#     if i % 5 == 0 and i % 6 ==0:
#         i += i
#         print(i)

#
# a = randint(1,100)
# b = randint(1,100)
#
# print(sqrt(min(a,b)))

# x = float(input('enter amount in GEL: '))
# currency = input('enter your currency: ')
# if currency == 'usd':
#     print(x / 2.88)
# elif currency == 'eur':
#     print(x / 2.85)

# number_1 = int(input('enter number one: '))
# number_2 = int(input('enter number two: '))
# for i in range(number_1,number_2+1):
#     if i % 5 == 0:
#         i += i
# print(i)

# year = int(input('enter your year: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year,'weli nakiania')
# else:
#     print(year, 'weli araa nakiani')


# x = input('enter your number: ')
# print (x[-1])

# x = int(input('enter number1: '))
# y = int(input('enter number2: '))
#
# for i in range(1,(min(x,y)+1)):
#     if x % i == 0 and y % i ==0:
#         gcd = i
# print((gcd))

#
# x = int(input('enter number: '))
# y= str(x)
# print(y[::-1])
#
# def fact(number):
#     return (factorial(number))
#
# print(fact(5))

# attampts = 3
# randnum = randint(1,10)
# for attampt in range(attampts):
#
#     user_number=int(input('enter your number: '))
#     if randnum < user_number:
#         print(f'you have bigger number {attampts - attampt -1} are left')
#     elif randnum > user_number:
#         print(f'you have smaller number {attampts - attampt -1} are left')
#     else:
#         print(f'you have correct number {attampts - attampt -1} are left')
#         break
# else:
#     print('you have used all attempts')
#

# def AVG(x = 1, y = 2, z = 3):
#     return (x+y+z)/3
#
# print(AVG())
# print(AVG(4,5,6))
# print(AVG(7,8,9))

# def calc(number):
#     return number**3
#
# print(calc(3))
# print(calc(5))

# def minimum(number1,number2):
#     return min(number1, number2)

# print(minimum(9,12))


# def number(num):
#     if num % 2 == 0:
#         return ('False')
#     return ('True')
#
# print(number(8))


# x = float(input('enter nimber1: '))
# y = float(input('enter nimber2: '))
# z = input('enter aritmetical symbol: ')
# if z == '*':
#     print(x * y)
# elif z == '/':
#     print (x / y)
# elif z == '+':
#     print(x + y)
# elif z == '-':
#     print(x - y)


# x = int(input('enter nimber1: '))
# y = int(input('enter nimber2: '))
# z = 1
# for i in range(x,y+1):
#     if i % 5 ==0:
#        k = i * z
#     print(k)


# x = 'hello'
# my_list = []
# for i in x:
#     my_list.append(i)
# print(my_list)

# numbs = [1,2,3,4,5]
# print(max(numbs))
# print(min(numbs))
# print(sum(numbs))
# print(sum(numbs)/len(numbs))
#
# numbs.append(102)
# print(numbs)
#
# numbs.insert(2,205)
# print(numbs)
#
# numbs.pop(3)
# print(numbs)
#
# numbs.sort()
# print(numbs)

# numbers = []
# for i in range(1,11):
#     a = int(input('enter your number: '))
#     numbers.append(a)
# print(len(numbers))
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

# a = [1,2,3]
# b = [5,6,4]
#
# def x(a,b):
#     for item in a:
#         if item in b:
#             return True
#     return False
#
# print(x(a,b))

# a = input("Enter your number: ")
# x = list()
# for i in a:
#     x.append(int(i))
# print(sum(x))
#
# extensions = ['txt', 'py', 'java', 'html']
# z = input('enter file name: ')
# x = z.split('.')
# def names(list1,list2):
#     for i in x:
#         if i in extensions:
#             return True
#         return False
#
# print(names(x,extensions))

# x = [4,5,9,3,7,2]
# random.shuffle(x)
#
# print(x)
#
#
# a = [1,2,3,4,5,6,7,8]
#
# def x(list1):
#     newlist = []
#     for i in list1:
#         if i % 2 != 0:
#           newlist.append(i)
#     return newlist
#
# print(x(a))
#

# list = [1,2,3,4,5,6,7]
# for i in list:
#     i += 15
#     print(i)

# x = input("Enter a number: ")
# y = []
# for i in x:
#     y.append(int(i))
# print(sum(y))


# x = [1, 5, 25, 15, 5, 4, 1, 2, 5, 7]
# for i in x:
#     z = x.count(i)
#     print(max(z))
#

# x = []
# for i in range(10):
#     y = random.randint(1,100)
#     x.append(y)
# print(x)
# a = max(x)
# b = min(x)
# print(a+b)

# x = [1, 10, 5, 8, 7, 3]
# x.sort()
# print(x)
# x.reverse()
# print(x)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def num(list):
#     newlist = []
#     for i in list:
#         if i % 2 != 0:
#             newlist.append(i)
#     return newlist
# print(num(x))

# x = [1, 2, 3, 4, 5]
# y = []
# for i in x:
#     i +=10
#     y.append(int(i))
# print(y)

# x = input("Enter a number: ")
# y = []
# for i in x:
#     y.append(int(i))
# print(sum(y))

# x = list()
#
# for i in range(10):
#     y = random.randint(25,110)
#     x.append(y)
# print(min(x))

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
#
# main_dict = dict1 | dict2 | dict3
# print(main_dict)
#
# my_dict = {'x':100, 'y':200, 'z':300}
# for key, value in my_dict.items():
#     print(key, '->', value)

# x = {}
# for i in range(1,11):
#     x[i] = i**2
# print(x)

# x = input('enter first word: ')
# y = input('enter second word: ')
# c = set(x)
# d = set(y)
# e = c.intersection(d)
# print(e)

# x = []
# for i in range(1,11):
#     y = random.randint(25,110)
#     x.append(y)
# print(sum(x)/len(x))

# x = input('enter your sentence: ')
# y = x.split(' ')
# print(y)

# x = [1, 2, 3, 4, 5 ]
# y = [6, 7, 2, 9, 10]
#
# def c(list1,list2):
#     for i in list1:
#         if i in list2:
#             return True
#     return False
#
# print(c(x,y))

# x = [i for i in range(100,200) if i % 5 == 0]
# print(x)

# name = input("Enter your name: ")
# last_name = input("Enter your last name: ")
#
# print(f'{name}.{last_name}@gmail.com')

# x =  'python,php,pascal,javascript,java,c++'
# delim = x.split(',')
#
# print(delim)

# set1 = {'first', 'second'}
# set2 = {'third', 'first'}
#
# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)
# set5 = set1.difference(set2)
# print(set5)
# set6 = set1.symmetric_difference(set2)
# print(set6)

# x = input("Enter a number: ")
# cou = 0
# for i in x:
#
#     if int(i) == 0:
#         cou += 1
#     else:
#         cou
# print(cou)

# x = input('enter first word: ')
# y = input('enter second word: ')
# if lower(x) == lower(y):
#     print(True)
# else:
#     print(False)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = []
# for i in x:
#     if i % 2 ==0:
#         y.append(i)
# print(x)
# print(y)

# x = float(input("Enter the value of x: "))
# y = [50, 20, 10, 5]
# for i in y:
#     if x % max(int(i)) == 0:


# # Define available bill denominations
# bills = [50, 20, 10, 5]
#
# # Get the amount of money from the user
# amount = float(input("Enter the amount of money you want to split: "))
#
# # Convert the amount to an integer number of cents
# # This avoids issues with floating-point precision
# amount_cents = int(round(amount * 100))
#
# # Initialize dictionary to store the number of each bill
# bill_count = {}
#
# # Calculate the number of bills needed for each denomination
# for bill in bills:
#     bill_cents = bill * 100
#     if amount_cents >= bill_cents:
#         count = amount_cents // bill_cents
#         amount_cents %= bill_cents
#         bill_count[bill] = count
#
# # Calculate the total number of bills used
# total_bills = sum(bill_count.values())
#
# # Print the results
# print(f"Number of bills: {total_bills}")
#
# print("The bills should be as follows:")
# for bill in bills:
#     if bill in bill_count:
#         print(f"{bill_count[bill]} {bill} GEL bill(s)")
#
# # If no bills needed, print a message
# if total_bills == 0:
#     print("No bills needed.")


#
# def nums_mult(*args):
#     x = 1
#     for i in args:
#         x *= i
#     return x
#
# print(nums_mult(1,2,3,4,5))

# z = {}
# x =  'python php pascal javascript java c++'
# y = x.split(' ')
# longest_word = ''
# length = 0
#
# for i in y:
#     if len(i) > length:
#         length = len(i)
#         longest_word = i
# print(longest_word, length)

# a = list()
#
# for i in range(1,11):
#     x = random.randint(1,100)
#     a.append(x)
# print(a)
# print(median(a))
# print(mode(a))

# a = int(input("Enter a number: "))
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i in d:
#     if a in d.values():
#         print()
# print(True)
#

#
# x = []
# y = []
# for a in range(1,11):
#     x.append(a)
# for b in range(1,11):
#     b= b ** 3
#     y.append(b)
# dict1 = dict(zip(x,y))
#
# print(dict1)


# x = input('first word: ')
# y = input('second word: ')
# set1 = set(x)
# set2 = set(y)
# s = set1.intersection(set2)
# print(s)

# x = []
# for i in range(1,11):
#     x.append(int(input('input your list')))
#     a = set(x)
# print(a)
#
# dict1 = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# for key, value in dict1.items():
#     print(key, "->", value)
#
# x = input("Enter 10 digit number: ")
# y = list(x)
# z = set(y)
# print(z)


# file = open('data.txt', 'r')
# content = file.read(100)
# print(content)
# file.close()

# with open('data.txt', 'r') as f:
#     for line in f:
#         print(line)
#
#

# file = open('data.txt', 'a')
# file.write('\niashiuaehfohafs')
# file.close()

# with open('data.txt','a') as file:
#     file.write('\nsahdlad')

# file = open('data.txt', 'r')
# print(file.tell())
# file.read(5)
# print(file.tell())
# file.seek(0)
# print(file.tell())


# if os.path.exists('data.txt'):
#     os.remove('data.txt')
#
# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter a number: "))
#     print(x / y)
# except ValueError as e:
#     print(e)

# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
# def ideal(x):
#     sum = 0
#     for i in range(1,x):
#         if x % i == 0:
#             sum += i
#     return (sum == x)
#
# file = open('test.txt','a')
# file.write(str(num))
#
# print(ideal(num))
#
# x = list()
# y = list()
# z = list()
# try:
#     for i in range(10):
#         a=random.randint(1,100)
#         x.append(a)
#     print(x)
#     y = list()
#     for i in range(10):
#         b=random.randint(1,100)
#         y.append(b)
#     print(y)
#     for i in range(len(x)):
#         if i % 2 == 0:
#             z.append(x[i])
#         else:
#             z.append(y[i])
# except ValueError as e:
#     print(e)
#
#     file = open('test.txt', 'a')
#     for i in z:
#         file.write(str(i)+'\n')
#     print(z)
#
#
# while True:
#     num1 = int(input('Enter num1 (to exit enter 0): '))
#     num2 = int(input('Enter num2 (to exit enter 0): '))
#
#     if num1 == 0 or num2 == 0:
#         break
#     def mir(num1, num2):
#         if str(num1)[0:] == str(num2)[::-1]:
#             return True
#         return False
#
# file = open('test.txt','w')
# file.write('True')
#
# print(mir(num1,num2))
#
#
#
# while True:
#     num = int(input("Enter a number(to exit input 0): "))
#     if num == 0:
#         break
#
# def optim(num):
#     mult = 0
#     for i in range(1,num):
#         if num % i == 0:
#             mult *= i
#             return True
#     return False
#
# file = open('test.txt', 'a')
# file.write(str(num))
# print(optim(num))
#
#
# while True:
#     x = input('enter your word: ')
#     if x =='finish':
#         break
# file = open('variant2.txt','a')
# file.write(x)
# file.close()

class Rectangle:
    '''
    this class is rectangle

    '''
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

rectangle1 = Rectangle(2, 3)
print(rectangle1.width, rectangle1.length)
print(type(rectangle1))
print(rectangle1.__doc__)
print(rectangle1.perimeter())