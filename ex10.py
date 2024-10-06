operacao = input('Selecione (+, -, %, /):')
num1 = float(input('numero 1:'))
num2 = float(input('numero 2:'))
i = ''

if operacao == '+':
    i = num1 + num2
elif operacao == '-':
    i = num1 - num2
elif operacao =='%':
    i = num1 % num2
elif operacao =='/':
    i = num1 / num2
else:
    i = f'Erro : {operacao}'

print(f'{i}')

