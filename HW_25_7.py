# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:49:29 2021

@author: Jitranjan GHOSH
"""
# Python Program for Creation of Numeric

##Creating Integer Data

a = 5
print("Type of a: ", type(a))
print(a)

##Creating Float Data
b = 1.5
print("\nType of b: ", type(b))
print(b)

##Creating Complex Data
c = 2 + 4j
print("\nType of c: ", type(c))
print(c)



# Python Program for Creation of String
    
## with single Quotes
String1 = 'I am Jitranjan Ghosh AKA Jit Ghosh'
print("\nString with the use of Single Quotes:: ")
print(String1, type(String1))
   
## with double Quotes
String1 = "I am Jitranjan Ghosh AKA Jit Ghosh"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1), type(String1))
   
## with triple Quotes
String1 = '''I am Jitranjan Ghosh AKA "Jit" Ghosh'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1), type(String1))
 
##Creating String with triple
### Quotes allows multiple lines
String1 = '''I am Jitranjan Ghosh 
    AKA 
Jit Ghosh'''
print("\nCreating a multiline String: ")
print(String1, type(String1))


## characters of String 
String1 = "Jitranjan Ghosh"
print("Initial String: ")
print(String1)
   
### Printing First character
print("\nFirst character of String is: ")
print(String1[0])
   
### Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

### Printing arbitary character
print("\nSeventh character of String is: ")
print(String1[6])

### Printing arbitary character
print("\nSeventh character of String is: ")
print(String1[-7])




# Python program to demonstrate List Creation
   
## Creating a Blank List
List = []
print("Initial blank List: ")
print(List)
   
## Creating a List with the use of a String
List = ['Jitranjan Ghosh AKA Jit Ghosh']
print("\nList with the use of String: ")
print(List)
   
## Creating a List with the use of multiple values
List = ["'Jitranjan", " Ghosh ", "AKA", "Jit Ghosh", "35+"]
print("\nList containing multiple values: ")
print(List)
print(List[0]) 
print(List[2])
print(List[3])

## Creating a List with the use of Positive Indexing
print("\nAccessing element from the list")
print(List[1]) 

## Creating a List with the use of Nagetive Indexing
print("\nAccessing element from the list using Negative Indexing")
print(List[-2])

## In case of List data can be Mutabile type
List[0] = 'Ranjan'
print(List)

## Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Jitranjan', 'Ghosh'], ['AKA'], ['Jit Ghosh']]
print("\nMulti-Dimensional List: ")
print(List)




# Tuple is ordered collection of Python object. Once createdc tuple data can not be mutilated
#### Tuple can be created with single data but data must trailing by a comma.

## Creating an empty tuple

Tuple1 = ()
print("Initial empty Tuple: ")
print (Tuple1)
   
## Creating a Tuple with the use of Strings
Tuple1 = ('Jitranjan', 'Ghosh')
print("\nTuple with the use of String: ")
print(Tuple1)
   
## Creating a Tuple with the use of list
list1 = [150, 293, 440, 525, 672]
print("\nTuple using List: ")
print(tuple(list1))
 
## Creating a Tuple with the use of built-in function
Tuple1 = tuple('Jit Ghosh')
print("\nTuple with the use of function: ")
print(Tuple1)
print('\n',Tuple1[1])
print('\n',Tuple1[-5])

## Creating a Tuple with nested tuples
Tuple1 = (0, 14, 24, 36)
Tuple2 = ('Jitranjan', 'Ghosh')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)



# Boolean is type of data with TWO built in value - TRUE or FALSE


# Python program to demonstrate boolean type
 
print(type(True))
print(type(False))
 
print(type(True))




#Set - It is a type of data without order, muitable, Iterable has no duplicate value.

## Python program to demonstrate Creation of Set in Python
   
## Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
   
## Creating a Set with the use of a String
set1 = set("Jitranjan Ghosh AKA Jit Ghosh")
print("\nSet with the use of String: ")
print(set1)
 
## Creating a Set with the use of a List
set1 = set(["Jitranjan", "Ghosh", "AKA", "Jit"])
print("\nSet with the use of List: ")
print(set1)
 
## Creating a Set with a mixed type of values (Having numbers and strings)
set1 = set([1, 2, 'Jitranjan', 4, 'Jit', 6, 'Ghosh'])
print("\nSet with the use of Mixed Values")
print(set1)



#Dictionary - It is also a data without order. Dictionary hold Key, valur pair, 
#Key Value pair separated by colon, Key separated by comma. It is Case sentative also.

## Python program to demonstrate Creation of Set in Python

## Creating an empty Dictionary
Dict = {}
print("Null Dictionary: ")
print(Dict)
   
## Creating a Dictionary with Integer Keys
Dict = {1: 'Jitranjan', 2: 'Jit', 3: 'Ghosh'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
   
## Creating a Dictionary with Mixed keys
Dict = {'Jit': 'Ghosh', 14: [40, 52, 63, 44]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

print("\n Accessing a element using key:")
print(Dict['Jit'])  

## Creating a Dictionary with dict() method
Dict = dict({1: 'Jit', 2: 'Ranjan', 3:'Ghosh'})
print("\nDictionary with the use of dict(): ")
print(Dict)
   
## Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Jitranjan'), (2, 'Jit')])
print("\nDictionary with each item as a pair: ")
print(Dict)
print("Accessing a element using get:")
print(Dict.get(3))

