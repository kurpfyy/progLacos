'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

num = float(input("Digite um numero (-1 encerra o programa)"))
maior = num
menor = num
total_respostas = 0
soma = 0
while ( num != -1):
    soma = soma + num
    total_respostas = total_respostas + 1
    if ( maior < num ):
        maior = num

    if ( menor > num ):
        menor = num


    num = float(input("Digite outro numero (-1 encerra o programa)"))

if ( maior == -1):
    print("Voce perdeu inseriou -1 na primeira resposta. \nPrograma encerrado :(")
else:
    print(f"Maior valor inserido é {maior}")
    print(f"Menor valor inserido é {menor}")
    print(f"a Media dos valores é {soma/total_respostas}")
    print("Fim do PROGRAMA")