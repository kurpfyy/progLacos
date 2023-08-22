"""
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
"""
'''
b = float(input("Informe a base de da potencia: "))
e = float(input("Informe a expoente da potencia: "))

# usuario -> b = 3, e = 4
# no papel -> 3 * 3 * 3 * 3
acumulador = 1
cont = 1
while ( cont <= e ):
    acumulador = acumulador * b
    cont = cont + 1

print(f"{b:.0f} elevado á {e:.0f} = {acumulador:.0f}")
'''

b = float(input("Informe a base de da potencia: "))
e = float(input("Informe a expoente da potencia: "))

pot = b ** e

print(f"{b:.0f} elevado á {e:.0f} = {pot:.0f}")


