'''
Código: IMC.
Autor: Raphael Comesanha
Período de Elaboração: Em 16/01/2020
O Código Executa: Solicita o peso e a altura do usuário e mostra na tela o valor do IMC daquele usuário.
Parte do Projeto:CeV_exercicios
Restições de acesso: Nenhuma
'''
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura) ** 2
print('Sue IMC é: {}!'.format(str(imc)))# Saída Formatada

