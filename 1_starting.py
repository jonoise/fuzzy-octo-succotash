"""
1- Los strings son inmutables, esta es la forma en la que se modifican.
1- Haciendo una lista y luego joining them.
"""

# string = "String"
# L = list(string)
# L[0] = "f"
# string = "".join(L)

# print(string)

"""
2- El join method es demasiado útil y polifacético.
2- Cosas muy interesantes se hacen con él.
2- Como separar los elementos de una lista por un caracter específico:
"""

# print("-".join(["A","B","C"]))


"""
3- Slicing is pretty neat aswell. We should learn slicing tricks.
3- Python docs:
"""
# word = "Python"

# # SIEMPRE en Python los índeces excluyen el último número.
# word[0:2]  # characters from position 0 (included) to 2 (excluded)

# print(word[-2:])


"""
4- El ejemplo uno (1) de esta lista, también lo podemos conseguir con slicing
4- creando una nueva palabra:
4- Ejemplo en el que hackeamos la palabra Alajuela.
"""

# word = "alajuela"
# pron = ['crack', "cac", 'font', 'par', "golf", 'agu', 'dest']

# def transforming_alajuela(word, prefixes):
#     final = []
    
#     for prefix in prefixes:
#         new = prefix + word[2:]
#         final.append(new)

#     return final

# final = transforming_alajuela(word, pron)

# for word in final:
#     print(word.find('crack'))
