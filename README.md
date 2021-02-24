# Estudiando programación competitiva con [este libro](https://www.amazon.com/Competitive-Programming-Python-Algorithms-Develop/dp/1108716822).

## 1_Starting.py notes:

En este archivo está el código del primer día. Dediqué gran parte del archivo a jugar con los tutoriales del sitio oficial de [Python](https://www.python.org). Entre los conceptos que refresqué están los slices.

## 2_second_day.py notes:

**n-tuples**: La "n" es por el "n" número de objetos que tiene dentro. Una tupla "1-tuple", al solo tener un valor debe ir acompañada de una coma: (1,).

**dictionaries**: Sirven para relacionar (mapear) *objectos* con valores. Los diccionarios son construídos como key:value pairs. Un diccionario vacío se obtiene con {}. Para verificar si una llave 'x' vive en el diccionario 'd' hacemos:
```python 
'x' in d
# Regresa True si 'x' es una llave en d.
```
OJO : Si las llaves de un diccionario son números del 0 al n-1, el uso de una lista es más eficiente.

**for loop**: El "for" loop es de los más útiles y versátiles. Es un loop tan sencillo que a veces cuesta digerirlo. La notación es:
 ```python 
for x in d:
    #aquí va tu código.

# Itera por todos los 'x' del 'd'. Si 'd' es un diccionario itera los keys, si 'd' es una lista itera el valor.
```

**while loop**: En contraste el 'while' loop aplicado en diccionarios o listas se efectuará hasta que estén vacíos.
```python 
while d:
    #aquí va tu código.

# Itera todos los valores de d (sea una lista o un diccionario).
```

A veces es necesario manejar los índices y los valores de una **lista** al mismo tiempo. Se puede implementar con el método enumerate():
```python 
for index, value in enumerate(d):
    # podemos hacer uso de ambas variables ahora.
```

Para tener acceso a los key:value pairs de un diccionario el código sería:
```python 
for key, value in d.items():
    # podemos hacer uso de ambas variables ahora.
```

# Comprensiones de listas y diccionarios.

## Comprensiones de Listas
Python ofrece sintaxis similar a la de las matemáticas para ciertos objetos. Las listas y diccionarios sirver para DESCRIBIR una serie de objetos. Para *describir* una **lista** con todos las raíces cuadradas de 0 a 'n al cudrado' se podría hacer:

```python
n = 5
raices = [x ** 2 for x in range(len(n+1))]
# cada número 'x' de 0 a 5 se va a elevar al cuadrado. si ven, 'raices' es una lista a la que le añadimos una expresión dentro.
```
También es particularmente útil para crear listas de 'n' tamaño.
```python
n = 5
lista = [0 for _ in range(n)]
# Crea una lista de 0's de 'len' n = 5.
```

## Comprensiones de Diccionarios

Como los diccionarios almacenan pares de información (key:values) las comprensiones de diccionario difieren mínimamente de las listas.
```python
mi_string = "Hello World"
d = {letra: 0 for letra in mi_string}
# en lugar de usar [] usamos {} porque queremos un diccionario. también asignamos un key:value -> 'letra: 0'.
```
Este código va a crear un 'key' por cada letra de 'mi_string' y le va a asignar el valor 0. De esta manera podemos usar un diccionario como una especie de contador de objetos.



