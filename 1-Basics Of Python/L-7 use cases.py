# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:24:53 2024

@author: Hp
"""

'''write a python program by using some logical oprators to 
check the height to allow for the roller coaster and also ask for the bills'''

print("Welcome to the Roller Coaster")

ht=int(input("Enter your height: "))
if ht>=120:
    print("You are eligible for the Roller Coaster")
    age=int(input("Enter Your age: "))
    bill=0
    if age<12:
        print("Your ticket is 5 Rs")
        bill=5
    elif age>12 and age<18:
        print("Your ticket is 20 Rs")
        bill=20
    elif age>18 and age<30:
        print("Your ticket is 30 Rs")
        bill=30
        
    want_photo=input("Ans us in Y or N: ")
    if want_photo=='Y':
        bill+=10
        print(f"Now Your bill will be: {bill}")
    elif want_photo=='N':
        print(f"Now Your bill will be: {bill}")
        
        
    want_popcorn=input("Ans us in Y or N: ")
    if want_popcorn=='Y':
        bill+=20
        print(f"Now Your bill will be: {bill}")
    elif want_popcorn=='N':
        print(f"Now Your bill will be: {bill}")
        
        
        
    else:
        print("Sorry you are not eligible")
else:
    print("Sorry you are not eligible")
    
'''
Welcome to the Roller Coaster
Enter your height: 120
You are eligible for the Roller Coaster
Enter Your age: 25
Your ticket is 30 Rs
'''


"""To calculate the BMI and show what is your physical condition"""
    
    
height=float(input("please enter your height in m:"))
weight=float(input("plaease enter your weight in kg:"))
BMI=round((weight/(height*height)),2)
BMI
if BMI<18.5:
    print(f"you are under weight and your BMI is:{BMI}")
elif BMI>18.5 and BMI<30:
    print(f"you are normal weight and your BMI is:{BMI}")    
elif BMI>25 and BMI<35:
    print(f"you are over weight and your BMI is:{BMI}")        
elif BMI>30 and BMI<35:
    print(f"you are obese weight and your BMI is:{BMI}")
elif BMI>35:    
    print(f"you are clinically obese weight and your BMI is:{BMI}")
    

    
# to find the duplicates fro m the list

lst=[5,6,8,1,4,2,2]
lst.sort()
lst

def is_duplicate(lst):
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:#compairing the cureent number fro the next one
            return True
    return False


print(is_duplicate(lst))

########################### AfterNoon#####################

#to find the leap year

year=int(input("Enter the year :"))
if(year%100==0 and year%400==0):
    print("YES Leap Year !")
elif(year%4==0 and year%100!=0):
    print("Yes Leap Year !")
else:
    print("Not A Leap Year !")
    
    
#mario pyramid 
#fav que of interviewer

row=int(input("Enter the num. of Rows: "))

for i in range(row):
    for j in range(i+1):
        print('*',end=" ")
    print()
    
#reverse mario pyramid


row=int(input("Enter the num. of Rows: "))

for i in range(row):
    for j in range(row-i):
        print('*',end=" ")
    print()
    
  #to finding minimun and max values

lst=[4,7,2,9,6] 

def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print(f"Your min value is: {min}") 
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print(f"Your max value is {max}")

min_max(lst)


#is palliantrome or not

input=input("step on no pets")

output=input[::-1]

if (input==output):
    print("Above string is Pallandome")
    
else:
    print("String is not Pallandrome")
    
    
def is_palindrome(input):
    if input==" ":
        return "You are entered wrong input"
    else:
         string=input[::-1]
         if string==input:
             return True
    return False

print(is_palindrome("step on no pets"))



#greetings to the posts

#users=["Admin","Employee","Manager","Worker","Staff"]
user=input("Please Enter your post:")
if user=="Admin":
    print("Hello Welcome Admin")
elif user=="Employee":
    print("Welcome Employee") 
elif user=="Manager":
    print("Welcome Manager")
elif user=="Worker":
    print("Welcome Worker")
else:
    print("Hello Sir")
    
    
#to create password
   
import string 
#to pick adjectives
adjectives=['sleepy','slow','wet','dry']
#to pick nouns
nouns=['apple','ball','goat','dragon']

import random

adjective=random.choice(adjectives)
noun=random.choice(nouns)
number=random.randrange(1,100)

spl_char=random.choice(string.punctuation)

passwords = adjective + noun + str(number) + spl_char
passwords

def lengths(itr):
    for ele in itr:
        yield len(ele)
    
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
'''ele*'*' appears to be the placeholder for the element from the
iterable  this asterisk * isused t replcae a letter as we are 
always see shen we are entering the password at any website
It's a generic representation that doesnt having any specific syntax'
'''
for password in hide(lengths(passwords)):
    print(password)
    

print("Welcome to the Picker!!")

while True:
    adjective=random.choice(adjectives)
    adjective=adjective.upper()
    noun=random.choice(nouns)
    noun=noun.upper()
    number=random.randrange(1,100)

    spl_char=random.choice(string.punctuation)

    password = adjective + noun + str(number) + spl_char
    print(password)
    response=input("Would u like to generate another password?")
    
    if response=='n':
        print("Thank You!!")
        break
    