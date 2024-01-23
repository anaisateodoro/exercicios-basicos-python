#3 - Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
quilometros = float(input("Digite a quantidade de quilômetros: "))
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10
print(f"\n{quilometros:.0f} quilômetros equivalem a:")
print(f"\n{metros:.0f} metros")
print(f"\n{centimetros:.0f} centímetros")
print(f"\n{milimetros:.0f} milímetros")