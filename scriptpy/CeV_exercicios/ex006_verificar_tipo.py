'''
Programa: Verificação de tipos
Autor:Raphael Comesanha
Período de Elaboração: 21/01/2020
Finalidade: Digitar algo e mostrar uma lista de características a respeito do que foi digitado.
Parte do Sistema: Nenhum
Restrições de segurança: Nenhuma
'''
a = input('Digite algo: ')
print('O tipo primitivo de {} é: '.format(a),type(a))
print('É só espaço em branco?-------------R = ', a.isspace())
print('É alfanumérico?--------------------R = ', a.isalnum())
print('É só numero?-----------------------R = ', a.isnumeric())
print('É só letra?------------------------R = ', a.isalpha())
print('Todos os caracteres são ASCII?-----R = ', a.isascii())
print('Está todo em maiúsculo?------------R = ', a.isupper())
print('Está todo em minúsculo?------------R = ', a.islower())
print('É um decimal?----------------------R = ', a.isdecimal())
print('Pode ser impresso?-----------------R = ', a.isprintable())
print('É um número digital?---------------R = ', a.isdigit())
print('Pode ser um identificado Python?---R = ', a.isidentifier())
print('Inicia com maiúscula?--------------R = ', a.istitle())
print('O valor digitado é composto de números({0}), Letras({1}), letras ou números ({2}) ou caracteres ASCII({3}).'.format(a.isnumeric(), a.isalpha(), a.isalnum(), a.isascii()))
