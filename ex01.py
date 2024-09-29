#String: str
print('-- String')
nomeCompleto = 'Nelson Luís Mussa'
cidade = 'Nampula'
pais = 'Moçambique'
print(f'Nome:{nomeCompleto}\nCidade:{cidade}\nPais:{pais}')

#Inteiro : int
print('-- Inteiro')
idade = 10
quantidade = 400
distancia = 200
print('Idade:{}\nQuantidade:{}\nDistancia:{}'.format(idade, quantidade, distancia))

#Real : float
print('-- Real')
altura = 1.6
salario = 2012.4
preco = 19.2
print('Altura: '+str(altura)+' Salário: '+str(salario)+' Preço:'+str(preco))

#Boolean: bool
print('-- Boolean')
estas_online = True
es_casado = False
es_estudante = True
print('Você estás Online: Sim' if estas_online else 'Você estás Online: Nào')