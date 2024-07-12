# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:20:55 2024

@author: Hp
"""
#to add the data items in the dictionary
car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}
car
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

car["color"]="white"
car
#dict_keys(['brand', 'model', 'year', 'color'])

x=car.keys()
x
#dict_keys(['brand', 'model', 'year', 'color'])

#how to remove the elements from the dictionary

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}

car.pop("model")
car
#{'brand': 'Ford', 'year': 1964}

#pop method is also used in the list but when we are removing the element from the 
#list it needs index only and here in dictionary it needs the name of key

#to access all the keys from the dictionary by using for loop

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}
for x in car:
    print(x)
    
#brand model year

#to access values from the dictionary then
for x in car:
    print(car[x])
    
# Ford Mustang 1964

# if we want to access keys and values from the dictionary

for keys,value in car.items():
    print("%s=%s" %(keys,value))
    
'''brand=Ford
model=Mustang
year=1964'''
  
#to copy the dictionary

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}
car2=car.copy()
car2#it will contain all the elements of dict car
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#another way to copy is to use the dict function

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}
car2=dict(car)
car2
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#nested dictionary=we can also have one or more ditionary inside the dict


family={"child1":
            {"name":"Ram",
             "DOB":"10-02-2004"},
        "child2":
            {"name":"Shyam",
             "DOB":"10-02-2004"}
        }    
family

'''{"child1":
            {"name":"Ram",
             "DOB":"10-02-2004"},
        "child2":
            {"name":"Shyam",
             "DOB":"10-02-2004"}
        }'''
    
#if u  want to remove all the entities from the dict there is a method called as clear

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}

car.clear()
#this will show the empty dictionary
car

#{}
    
# to create the dictionary from the fromkeys method

x={"key1","key2","key3"}
y=0
thisdict=dict.fromkeys(x,y)
thisdict

#{'key2': 0, 'key3': 0, 'key1': 0}

car={"brand":"Ford",
     "model":"Mustang",
     "year":1964}
car.items()
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


#values() its will going to give u all the values of dict

car.values()
#dict_values(['Ford', 'Mustang', 1964])

#update()=is use to insert the key and the value into the dict

car.update({"color":"white"})
car
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}

####################################################################################
#####################################################################
#use of break statement in for loop

fruits=["apple","cherry","banana","orange"]

for fruit in fruits:
    print(fruit)
    if (fruit=="banana"):
        break
    
'''
apple
cherry
banana
'''

fruits=["apple","cherry","banana","orange"]

for fruit in fruits:
    if (fruit=="banana"):
        break
    print(fruit)
    
'''
apple
cherry
'''

#use of continue statement

fruits=["apple","cherry","banana","orange"]

for fruit in fruits:
    if (fruit=="banana"):
        continue
    print(fruit)
'''apple
cherry
orange''' 
# it is just drop the banana and the next will continue
  
######################## AFTERNOON ###################################

#function witout argument
def my_function():
    print("hello from a function")
my_function()

#function with argument
def my_function(name):
    print("hello " +name)
    
my_function("ram")

def my_function(name1,name2):
    print(name1+" "+name2)
my_function("world","hello")

##############################################
#if we dont know how many argument we have to use that time arbitary argument is used
#add a* before the parameter name

def my_function(*kids):
     print(kids[0]+" "+kids[2])
     
my_function("hello","world","india") 

###############################################################################3
def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))
myFun(first='papalal', mid='mohanlal',last='goyal')

#we can use any other argument at place of kwargs

####################################################33
#default parameter
#it uses the default value
#if we call function without argument
def my_function(country= "naorway"):
    print("I am from "+country)

my_function("swedon")
my_function("India")
my_function()
my_function("brazil")    
################################################################
#passing a list as arguments
#you can send a list as an argument
fruits=["orange","banana","guava"]
def my_dict(fruits):
    for x in fruits:
        print(x)
my_dict(fruits) # hare we can use other words at place of function
# it will also execute
my_function(fruits)

####################################################################
# return values
#to let a function return a value,use the return statement
def my_function(x):
    return x*5
my_function(5) 

#pass function
def my_function():
    pass
#having an empty function definition
#like this would raise an error
#without the pass statement
########################################################################

#calling function inside a function recursive function 
#factorial of a num is the product of all integer
#from 1 to that num
def factorial(x):
    if x==1:
        return 1 
    else:
        return(x*factorial(x-1))
    
 
factorial(3) 
factorial(6)


######################################################################
#lambada function very important
# small anonymous function
#lambada function can take any no of argument
#but can only have one expression
#lambada function can take any no of arguments 
def add(a):
    sum=a+10
    return sum
add(20)
###########################
add=lambda a:a+10
print(add(20))

add=lambda a,b:a+b
print( add(5,6))  

#############################################333
#findind odd no from list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 !=0),lst))
print(odd_lst) 

# the filter is fuinction which is except your function
#when we want use iterator that time use Filter
#filter is used with iterator that is list
#it is used when we want to check whether the funtion is boolean i.e true or false

lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 !=0),lst))
print(odd_lst) 

#we use map function for sqr any no 
lst=[1,2,3,4,5,6,7,8,9,10]
sqr_lst=list(map(lambda x:(x**2 ),lst)) 
print(sqr_lst)
