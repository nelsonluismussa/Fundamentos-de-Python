#Operadores Aritméticos
# +, -, *, /,**, //, %, sqrt, pow

a1 = 10
b1 = 3

print(f'Adicção: {a1 + b1}')
print(f'Subtração: {a1 - b1}')
print(f'Multpilicação: {a1 * b1}')
print(f'Divisão Comum: {a1 / b1:.1f}')
print(f'Divisão Com Quociente: {a1 // b1}')
print(f'Módulo: {a1 % b1}')
print(f'Exponecial: {a1 ** b1}')
print(f'Raiz: {a1 ** (1/2) }')

import math
print(f'Raiz: {math.sqrt(a1)}')
print(f'Exponecial {math.pow(a1, 2)}')


#Operadores Relacional
# !=, ==, >, <, >=, <=
print((3 != 4))


#Operadores Lógico
# and, or, not
print( (4 >= 3) and not( 13==7) > (8))



#Operadores ternários
es_estudante = True
print('Estás é estudante: Sim' if es_estudante else 'Estás é estudante: Nào')