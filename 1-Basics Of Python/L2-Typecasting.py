# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:12:36 2024

@author: Hp
"""
#convertion of string to integers 
#it is called as typecasting
""" when we are taking input by default it is in the string form 
so to convert the declared variables in integer  

"""

age=input("Enter your age:")
print(age)
print(type(age))

age1=input("Enter your age:")
print(age1)
print(type(age1))

age2=input("Enter your age:")
print(age2)
print(type(age))

age=age1+age2
print(age)
print(type(age))

#after typecasting
age=int(input("Enter your age:"))
print(age)
print(type(age))

age1=int(input("Enter your age:"))
print(age1)
print(type(age1))

age2=int(input("Enter your age:"))
print(age2)
print(type(age))

age=age1+age2
print(age)
print(type(age))
#############################################################

#Floating Point Numbers
""" Real numbers or floating point numbers are represented 
in python"""

exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))
###############################################################
#converting to floats
"""as with integers it is possible to convert types such as an 
int or string into a float numbers"""

int_val=100
float_val=float(int_val)
print('int value as a float',float_val)
#int value as a float 100.0
print(type(float_val))
#<class 'float'>

str_val='1.03'
float_val1=float(str_val)
print('String value as a float',float_val1)
#String value as a float 1.03
print(type(float_val1))
#<class 'float'>
###############################################################
#complex numbers

c1=2
c2=3j
print('c1:',c1,'\nc2:',c2)
#c1: 2 
#c2: 3j
print(type(c1))
#<class 'int'>
print(type(c2))
#<class 'complex'>
print(c1.real)
#2
print(c2.imag)
################################################################
#Boolean Values
"""python supporters another type caled as Boolean
a boolean tye can only be one of True or false"""
all_ok=True
#True
print(all_ok)

All_Ok=False
print(All_Ok)
#False
print(type(All_Ok))
#<class 'bool'>
#################################################################

"""We can also convert the strings into booleans and output will
be in the form of True or False"""

status=bool(input('Ok Is it Confirmed?'))
#if u are giving any input the status will be True and if we not giving 
#any input then the status will be False
print(status)
print(type(status))
###################################################################
#Arithematic Operators
'''this is used to perform some form of mathematical operation such 
as addistion, substraction,multiplication and the division'''

home=14
away=7
print(home+away)#21
print(type(home+away))#<class 'int'>

print(home*away)#98
print(type(home*away))#<class 'int'>

print(home-away)#7
print(type(home-away))#<class 'int'>

'''however you may notice that we have missed out
division with resoect to integers
'''
print(100/20)#5.0
print(type(100/20))#<class 'float'>