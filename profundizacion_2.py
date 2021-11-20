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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print('A continuacion, se le pedira que ingrese 3 numeros enteros: ')

numero1 = int(input('Ingrese su primer numero: '))
numero2 = int(input('Ingrese su segundo numero: '))
numero3 = int(input('Ingrese su tercer numero: '))

if numero1 % 2 == 0:
    print('El numero {} es par'.format(numero1))
else:
    print('El numero {} es impar'.format(numero1))

if numero2 % 2 == 0:
    print('El numero {} es par'.format(numero2))
else:
    print('El numero {} es impar'.format(numero2))

if numero3 % 2 == 0:
    print('El numero {} es par'.format(numero3))
else:
    print('El numero {} es impar'.format(numero3))
