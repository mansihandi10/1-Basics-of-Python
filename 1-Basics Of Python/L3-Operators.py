# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:13:52 2024

@author: Hp
""" 

""" to ignore the fractional part the there is an alternativ
verwsion of divide operator is '//' when we will use these operator then
the output will be in the form of integer"""

print(100//20)#5
print(type(100//20))#<class 'int'>

"""but what is there are only intrested in the remainder
part of a division,the integer division operator is %"""
print('modulous division of 100%13:',100%13)#9(remainder of a div)

print('modulous division of 3%2',3%2)#1(remainder of a div)

"""a final integer operator we will look is the power operator 
that can be used as **
"""
a=5
b=3
print(a**b)#125
#Assignment Operator

"""These assignment operator are actually referred to as a compound
operator as they combine together a numeric operator with assignment 
operator, for example the += compund operator is the combination of
add and equal
"""
x=9
x+=1 #it will behave like a x=x+1
x#10

#None Operator
"""Python is case sensitive so it having some special operator"""
Winner=None
print("Winner is  None",Winner is  None)#True

Winner=None
print("Winner is not None",Winner is not None) #False

print(type(Winner))
#<class 'NoneType'>
#####################################################

#Comparision Operators
'''before exploring if statementas we nees to discuss about the
comparisiob operators these operators that return boolean values
'''
'''note that indentation this is very important layout of the code
is also very important part '''

num=int(input("Enter the Num:"))
if num>0:
print(num)
# when we write the code without indentation the it will show you an error

#following is the right way to write the code with indentation
num=int(input("Enter the Num:"))
if num>0:
    print(num)
#Enter the Num:10
#10

#if else statement
num=int(input("Enter the Num:"))
if num<0:
    print(num,"is negative")
else:
   print(num,"is positive")
#Enter the Num:-9
#-9 is negative

#Enter the Num:35
#35 is positive

#use of elif

savings=int(input("Please Enter your savings"))
if savings==0:
    print("Sorry No Savings")
elif savings<500:
    print("Well Done")
elif savings<1000:
    print("That's a tidy Sum")
elif savings<10000:
    print("Welcome Sir")
    
else:
    ("Thank You Sir")
    
"""Please Enter your savings999
That's a tidy Sum"""

#to find the leap year

year=int(input("Enter the year :"))
if(year%100==0 and year%400==0):
    print("YES Leap Year !")
elif(year%4==0 and year%100!=0):
    print("Yes Leap Year !")
else:
    print("Not A Leap Year !")
######################################################

#Iteration and Looping

#while loop
'''the while loop is exists in almost all the programming
language  '''

count=1
print('Strting')
while count<=10:
    print(count)
    count+=1
# 1 to 10

##########################################################
# for loop

for i in range(2,10):
    print (i)
print('Done')
'''2
Done
3
Done
4
Done
5
Done
6
Done
7
Done
8
Done
9
Done'''

for i in range(2,10):
    print (i)
print('Done')
'''2
3
4
5
6
7
8
9
Done'''
###################################################

print('Only print the code if all the iterations are comleted')
n=int(input("Enter the number: "))
num=int(input("Enter any  number: "))
for i  in range(0,n+1):
    if i ==(num+1):
        break
    print(i)
print('Done')
'''Enter the number: 15
Enter any  number: 10
0
1
2
3
4
5
6
7
8
9
10
Done'''

#use of anonymous variable
#to avoid space complexity it is used
for _ in range(0,10):
    print('.')
 """.
    .
    .
    .
    .
    .
    .
    .
    .
    ."""
    
for _ in range(0,10):
    print('.',end=' ')
    print()#..........
    