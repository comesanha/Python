
#Aula 1 de Python
'''
data: 14/01/2020
Assuntos: Como utilizar a função print com , e o +, usar variaveis, atribuir
valores a variaveis com operador = (recebe), como utilizar a função input e
como criar scripts separados para posterior execução e inserção de comentários
simples e múltiplos.
'''
'''
print('Olá, Mundo')
print(7+4)
print('7'+'4')
print('7','4')
print('Olá',5)

nome = input('Qual é o seu nome?')
idade = input('Qual a sua idade?')
peso = input('Qual é o seu peso?')
print(nome, idade, peso)
'''
#Desafio 1
'''
Faça um script python que leia o nome de uma pessoa e e mostre uma mensagem
de boas-vindas de acordo com o valor digitado. 
'''
'''
usuario = input('qual seu nome de usuário?')
print('Bem vindo,',usuario+'!')
print('Cadastro realizado com sucesso!')
'''

#Desafio 2
'''
Crie um script pytho que leia o dia, o mês e o ano do nascimento de uma pessoa
e mostre uma mensagem com a data formatada.
'''
'''
dia = input('Qual o dia de seu nascimento?')
mes = input('Qual o mês de seu nascimento?')
ano = input('Qual o ano de seu nascimento?')
print('A sua data de nascimeto é',dia+'/'+mes+'/'+ano+'.','Correto?')
'''
#Desafio 3
'''
Crie um script python que leia dois números e mostre a soma entre eles.
'''
'''
a = input('Digite o pripeiro número.')
b = input('Digite o segundo número.')
s = int(a)+int(b)#conversão string para inteiro
s = str(s)#Conversão de inteiro para string
print('A soma entre eles é'+s)
'''
