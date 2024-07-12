# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:46:23 2024

@author: Mansi Handi
"""
#python program to print odd number in give range 
start, end=1,19
for num in range (start,end+1):
    #checking conditions 
    if num%2!=0:
        print(num,end=" ")
#1 3 5 7 9 11 13 15 17 19 
############################################      
#python program for a even number
start, end=4,19
for num in range (start,end+1):
    #checking condition
    if num%2==0:
        print(num,end=" ")
#2 4 6 8 10 12 14 16 18         
#############################################
#global variables
x="awesome"
def my_function():
    print("python is"+ x)
my_function()
#python is Awesome

############################################
x,y,z=5,6,7
print(x)
print(y)
print(z)
#############################################
x,y,z=5
print(x)
print(y)
print(z)

############################################
#local variable 
x="awesome"
def my_funcation():
    x="fantastic"
    print("python is "+x)
my_funcation()
print("python is "+x)

#to get the datatypes
x=5
print(type(x))
#<class 'int'>

x=range(6)
print(type(x))
#<class 'range'>

x={"name":'ram',"age":34}
print(type(x))
#<class 'dict'>

#when we are going to concadinate both the variables should be string 
#we can not concadinate one string and another integer variable#
str1="Hello"
str2=2
print(str1+str2)#this will show us an error
#""can only concatenate str (not "int") to str""
##########################################################
#string

#when we want multiple sentences then we should use '"""....."""'like this
x="""This is Python. It is very Powerful"""
print(x)
#"""This is Python. It is very Powerful"""

#string slicing
x="""This is Python. It is very Powerful"""
print(x[2:8])#is is 
#this will only print from 2nd letter of sentence to 7th letter of sentence

#slice from the start
print(x[:4])#This
#this will print only starting of 4 letters from the sentence

#slice from end
print(x[4:])#is Python. It is very Powerful
#this will only print the endling latters after the 4rth letter of the sentence

#negative slicing
print(x[-5:-2])
#erf

print(x[:-2])
#This is Python. It is very Powerf

print(x[-5:])
#erful
################################################################

#modification of the strings

print(x.upper())
#THIS IS PYTHON. IT IS VERY POWERFUL
#this will show the output as all the alphabates of the sentence will be capital letters

print(x.lower())
#this is python. it is very powerful 
#this will show the output as all the alphabates of the sentence will be in small letters


#to remove the empty or extra spaces fom the sentence strip function is used
x="   This is Python"
print(x.strip())#this funvtion will show uds the proper formate of the sentence
#This is Python

#there are another two functions like lstrip and rstrip 
#lstrip is for to remove the spaces of left side
#rstrip is for to remove the spaces of right side
x="   This is Python"
print(x.lstrip())

x="This is Python.                           "
print(x.rstrip())
#to replace any word replace func. is used

y="Hello Mansi"
print(y.replace("Mansi","Adarsh"))
#Hello Adarsh

#by using split which can separte the two words

y="Hello Adarsh"
print(y.split(" "))
#['Hello', 'Adarsh']

##########################################################

#######  AFTERNOON SESSION #############################
#reversing of string
# it is also used in the NLP
x="Hello Adarsh"
print(x[::-1]) #this will show the reverse of the variable
#hsradA olleH

x="Hello Adarsh"
print(x[::-2])#this will show thw reverse output in the step of -2
#hrd le

#find,searches of the string for a specified value

x="This is Python and it is very Powerful"
print(x.find("and"))
#it is on the place of 15

########################################
#string concateness
x="Hello"
y="World"

print(x+y)
#HelloWorld

# to add some spaces
x="Hello"
y="World!!"

print(x+" "+y)
#Hello World!!

#### String formation

x=20
y="My name is Mansi"

print(f"{y} and my age is {x}")
#My name is Mansi and my age is 20
#when we are concatinate string with the integer then it will give error
#but at same operation we done with the help of f operator
#it will give u proper output

# we can also concatinate multiple integers in the string

quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number {item_no}, its price is {price}")
#I want 3 pieces and item number 54 and its price is 67

#another method to it by using format operator
my_order="I want {} pieces and item number {}, its price is {}"
print(my_order.format(quantity,item_no,price))

#we can also give it as a variable ID number
quantity=3
item_no=54
price=67
my_order="I want {0} pieces and item number {1}, its price is {2}"
print(my_order.format(quantity,item_no,price))
#I want 3 pieces and item number 54, its price is 67

#some escape characters like back slash will allows us tp use double quotes

text="My name is \"MAnsi\"and my age is\"20\""
text
#'My name is "MAnsi"and my age is"20"'


#it is very important rule for the mathematical operator
print(3*3+3/3-3)#7.0
"""
PEMDAS
Paranthesis
Exponential
Multiplication
Division 
Addition
Substraction
"""




