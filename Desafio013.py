print('Desafio013: Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento:')

salario = float(input('Digite seu salário:R$ '))

aumento = float(salario * 0.15)
valor = salario + aumento

print('Seu salario antigo era de R${:.2f}, com um aumento de 15% você começara a receber um total de R${:.2f}' .format(salario, valor))
