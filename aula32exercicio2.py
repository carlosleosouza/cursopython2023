"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número: ')

if entrada.isdigit(): #Verifica se o usuário digitou um número inteiro, pois aqui não há conversão pra string
    resto = int(entrada) % 2
    if resto == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
else:
    print('Você não digitou um número inteiro')
    
    

    
