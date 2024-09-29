nota1 = 10
nota2 = 10

media = (nota1 + nota2) / 2
informacao = ''

if (media <= 4):
    informacao = f'Excluido com {media}'

elif (media >= 5.0 and media <= 6.5):
    informacao = f'Está em recuperação com {media}'

elif (media >= 6.6 and media <= 10):
    informacao = f'Dispensado com {media}!'

else:
    informacao = 'Inválido!'
    
print(informacao)
