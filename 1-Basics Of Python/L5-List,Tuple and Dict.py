# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:52:40 2024

@author: Hp
"""
#holypython.com
#python List

lst=["cherry","banana","apple"]
print(lst)

#['cherry', 'banana', 'apple']

#we can also access by using indexed 
print(lst[0])#cherry
print(lst[1])#banana
print(lst[2])#aple

#to add thwe items in the list we are using the function append()

lst.append("Mango")
lst
#['cherry', 'banana', 'apple', 'Mango']

#to clear and remove all the elements from the list
lst.clear()
lst
# [] then we will get the empty list

#copy method

lst=["cherry","banana","apple"]
lst1=lst.copy()
lst1
#it is use to copy the data from snotjer list
#['cherry', 'banana', 'apple']

#list having one feacher where it consist of variety of data type and it 
#having also another feacher like itb can contain repeated data

lst=["cherry","cherry","apple"]
lst.count("cherry")
#2 this is use to count the frequency of that item

lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)
#[1, 2, 3, 4, 5, 6]
#to add both the list in one

#insert method is use to insert the value in specific location
#also called as mutation which means we can change the data entities

lst=["cherry","cherry","apple"]
lst.insert(1,"Mango")
lst
#['cherry', 'Mango', 'cherry']


#pop() which is use to remove the entity from the list
lst=["cherry","cherry","apple"]
lst.pop(2)#in this method we are using index
lst
#['cherry', 'cherry']

#remove() it is also used to remove the entity from the list

lst=["cherry","cherry","apple"]
lst.remove("cherry")#in this method we are directly giving the name of the entity which we want to remove
lst#['cherry', 'apple']


#to reverse the entities of the list
lst=["cherry","cherry","apple"]
lst.reverse()
lst
#['apple', 'cherry', 'cherry']

#to sort the list alphabetically we can use the sort() function


lst=["cherry","orange","banana"]
lst.sort()
lst
#['banana', 'cherry', 'orange']
########################################################
###########################################################
############################################################
#Tuple
tup=("cherry","cherry","banana")
tup#('cherry', 'cherry', 'banana')
tup[2]#'banana'

#once a tupple is created it can not be changed it is also called as it is immutable

x=("cherry","cherry","banana")
x[1]='kiwi'

#to chage the tuple initially we have to convert that tuple into the tuple

y=list(x) #we converted this tuple into the list
y#("cherry","cherry", "banana")

y[1]='kiwi'#then added kiwi at a specific location
y#['cherry', 'kiwi', 'banana']

x=tuple(y)#and again we converted that list into the tuple
x('cherry', 'kiwi', 'banana')

# tuple has one another feachwer is that it can contain more that one data types

x=("cherry",2,"banana")
x
#('cherry', 'kiwi', 'banana')


#to join one and more tuple  we just use to + operator

tup1=("a","b","c")
tup2=(1,2,3)
tup=tup1+tup2
tup
#('a', 'b', 'c', 1, 2, 3)

#########################################################
#########################################################
#########################################################

#DICTIONARY

dict={"Brand":"Maruti","Model":"2345","Year":2011}
dict
#{'Brand': 'Maruti', 'Model': '2345', 'Year': 2011}
len(dict)
#3 
type(dict)
#dict

# we can also implement our complete table i the form of dictionary

dict={"Brand":["Maruti","Mahindra","suzuki"],
      "Model":["a","b","c"],
      "Year":[2011.2013,2022]}
dict
'''{'Brand': ['Maruti', 'Mahindra', 'suzuki'],
 'Model': ['a', 'b', 'c'],
 'Year': [2011.2013, 2022]}'''

dict.get("model")
dict.keys()
#dict_keys(['Brand', 'Model', 'Year'])

