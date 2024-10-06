

contador = 1
num = 1
soma = 0
resp = 'S'

while resp !='N':
    num = int(input(f'Números pesetivos {contador}:'))
    soma +=num
    contador +=1
    resp = str(input('Deseja continuar [S/N]:'))
print(soma)