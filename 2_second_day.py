"""
Dicts
"""
# # declarando un dic
# d = {'x':1}
# # asignando valores a una llave
# d['x'] = 2

# # imprime el valor guardado en "x".
# print(d['x'])

"""
List and Dicts comprehensions:
Los siguientes fueron ejercicios tomados de internet y las respuestas elaboradas por mi, es myt probable que diferamos en la
forma de plantear la solución porque hay más de una manera de responder correctamente a la pregunta.
Ejercicios tomados de https://holypython.com/intermediate-python-exercises/exercise-16-python-list-comprehensions/
"""

# Hacer una lista que tenga los números pares del 0 al 100
pares = [x for x in range(101) if x % 2 == 0]

# Crear una copia idéntica de una lista anteriormente creada (usando 'pares').
copy = [x for x in pares]

# Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
steps = [x for x in range(1200, 2001, 130)]

# Use list comprehension to contruct a new list but add 6 to each item.
list1=[44,54,64,74,104]
plus_six = [x + 6 for x in list1]

# Using list comprehension, construct a list from the squares of each element in the list.
list1=[2, 4, 6, 8, 10, 12, 14]
squares = [x ** 2 for x in list1]

# Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
list1=[2, 4, 6, 8, 10, 12, 14]
squares = [x ** 2 for x in list1 if x ** 2 > 50]

# Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles 
# with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
light_weight = [key for key in dict.keys() if dict[key] < 5000]

# Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.
list1=["NY", "FL", "CA", "VT"]
destinations = {x:x for x in list1}

# First, create a range from 100 to 160 with steps of 10.
# Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.
r = range(100, 161, 10)
divided = {x:x/100 for x in r}

# Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs 
# with value above 2000 are taken to the new dictionary.
dict1 = {"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2 = {x:dict1[x] for x in dict1 if dict1[x] > 2000}
