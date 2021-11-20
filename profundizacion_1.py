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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print('A continuacion, se le pedira que ingrese 2 numeros')

numero1 = float(input('Ingrese su primer numero: '))
numero2 = float(input('Ingrese su segundo numero: '))

diferencia = numero1 - numero2

if diferencia > 0:
    print('La diferencia es positiva:' ,diferencia)
elif diferencia <0:
    print('La diferencia es negativa:' ,diferencia)
else:
    print('La diferencia es: 0')