'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:

Considerando como exemplo o fornecimento do número 2
'''

num = int(input("Me diga qualquer numero inteiro:"))

contador = 1


while (contador <= 10):
    sum = num * contador
    print(f"{num}.{contador} = {sum}")
    contador = contador + 1