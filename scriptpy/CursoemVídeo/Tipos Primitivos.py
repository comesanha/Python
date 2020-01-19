'''
Programa: Tipos Primitivos
Autor:Raphael Comesanha
Período de Elaboração: 19/01/2020
Finalidade: Mostar o tipo da variável; converter uma variavel de um tipo para outro; Revisão de variavel formatada;
            concatenção de strings; mostrar variaveis interligadas e de tipos diferentes na tela. (máscara);
            verificação de tipo e ecaracterísicas de variaveis string (.is___) e atribuição da saída da verificação a
            uma variável.
Parte do Sistema: Nenhum
Restrições de segurança: Nenhuma
'''
'''
n1 = input('Digite um valor: ')
print(type(n1)) # Mostra o tipo da variável   
'''
'''
n1 = int(input('Digite um valor: '))    # Conveter para o tipo primitivo inteiro. caso não seja aribuido nenhum valor
                                        # ocorre erro na conversão. Exceto na função bool() - conversão para booleano.
print(type(n1)) 
'''
'''
n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
s = n1 + n2 # Concatena as strings n1 e n2
print('a soma dos valores digitados é: ',s)
'''
'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 # Soma dos inteiros n1 e n2
print('a soma dos valores digitados é: ',s)
'''
'''
n1 = int(input('digite um número: '))
n2 = int(input('Digite outro número'))
s = n1 + n2
#print(' A soma entre ',n1,' e ',n2,' é: ', s)
print('a soma de {} com {} é: {}'.format(n1, n2, s))    # mostra valor da variavel formatada dentro da Mascara (chaves).
'''
'''
n = float(input('Digite um Valor: '))
print(type(n))
print(n)    # Mostra o valor digitado convertido em ponto flutuante.
'''
'''
n = str(input('Digite um Valor: ')) # Mesmo que não utilizar a função. O valor permanece com o tipo string.
print(n)
print(type(n))
'''
'''
n = bool(input('Digite um valor: '))    # Converte a variavel para o tipo primitivo booleano. Se for atribuido algum 
                                        # valor a variavel ela recebe o valor True, se não for atribuido nenhum valor,
                                        # ela recebe o valor False.
print(type(n))
print(n)
'''
'''
n = input('Digite algo: ')
print(n.isnumeric())  # Verifica se é possível convertes o que foi digitado em número com o tipo primitivo int.
'''
'''
n = input('Digite algo: ')
print(n.isalpha())  # Verifica de o que foi digitado é letra.
'''
'''
n = input('Digite algo: ')
print(n.isalnum())  # Verifica se o que foi digitado é alfanumérico.
'''
'''
n = input('Digite algo: ')
print(n.isupper())  # Verifica se o que foi digitado está em caixa alta.
'''
'''
Desafio 3: Crie um programa que leia dois números e mostre a soma entre eles.
# Solução
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = a + b
print('A soma entre {} e {} é igual a {}.'.format(a, b, c))
'''
'''
Desafio 4: faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas a informações 
possíveis a respeito daquilo que foi digitado.
# Solução
d = input('DIgite algo: ')
# e = d.islower() + d.isupper() # Atribui o valor lógico de saída do .is__ a variavel "e".
print('É um numero?-------------R = {}'.format(d.isnumeric()))
print('É uma letra?-------------R = {}'.format(d.isalpha()))
print('É alfanumérico?----------R = {}'.format(d.isalnum()))
print('Está em caixa alta?------R = {}'.format(d.isupper()))
print('Está em letra minúscula?-R = {}'.format(d.islower()))
print('Está no padrão ASCII?----R = {}'.format(d.isascii()))
print('É valor lógico?----------R = {}'.format(d.isdigit()))
print('É um decimal?------------R = {}'.format(d.isdecimal()))
print('É um espaço em branco?---R = {}'.format(d.isspace()))
print('É um imprimível?---------R = {}'.format(d.isprintable()))
'''
