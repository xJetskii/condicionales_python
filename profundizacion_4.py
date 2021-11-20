# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra1 = str(input('Ingrese la primer palabra: '))
palabra2 = str(input('Ingrese la segunda palabra: '))
palabra3 = str(input('Ingresar la tercer palabra: '))

print('Elija como ordenar las palabras: ')
print('1-Ordenar por orden alfabetico')
print('2-Ordenar por cantidad de letras')

opcion = int(input())


if opcion == 1:
    if palabra1 > palabra2:
        if palabra1 > palabra3:
            if palabra2 > palabra3:
                print(palabra3, palabra2, palabra1)
            else:
                print(palabra2, palabra3, palabra1)
        elif palabra3 > palabra1:
            print(palabra2, palabra1, palabra3)

    elif palabra2 > palabra1:
        if palabra2 > palabra3:
            if palabra3 > palabra1:
                print(palabra1, palabra3, palabra2)
            else:
                print(palabra3, palabra1, palabra2)
        else:
            print(palabra1, palabra2, palabra3)


elif opcion == 2:
    if len(palabra1) > len(palabra2):
        if len(palabra1) > len(palabra3):
            if len(palabra2) > len(palabra3):
                print(palabra1, palabra2, palabra3)
            else:
                print(palabra1, palabra3, palabra2)
        elif len(palabra3) > len(palabra1):
            print(palabra3, palabra1, palabra2)

    elif len(palabra2) > len(palabra1):
        if len(palabra2) > len(palabra3):
            if len(palabra3) > len(palabra1):
                print(palabra2, palabra3, palabra1)
            else:
                print(palabra2, palabra1, palabra3)
        else:
            print(palabra3, palabra2, palabra1)