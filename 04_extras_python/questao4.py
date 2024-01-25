"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
"""
def euro(valor):
    valor_converter = valor / 5.36
    return float("{:.2f}".format(valor_converter))

def libra(valor):
    valor_converter = valor / 6.21
    return float("{:.2f}".format(valor_converter))

def dolarAME(valor):
    valor_converter = valor / 4.91

    return float("{:.2f}".format(valor_converter))

def PesoARG(valor):
    valor_converter = valor / 0.02
    return float("{:.2f}".format(valor_converter))

def dolarAUS(valor):
    valor_converter = valor / 3.18
    return float("{:.2f}".format(valor_converter))

def dolarCAN(valor):
    valor_converter = valor / 3.64
    return float("{:.2f}".format(valor_converter))

def francoSUI(valor):
    valor_converter = valor / 0.42
    return float("{:.2f}".format(valor_converter))

val = float(input("\nValores em reais para conversão: R$"))
print('***************************************************')
print (f"Tabela de conversão:")
print('*****************************')
print (f"Dólar Americano: ${dolarAME(val)}\nPeso Argentino: ${PesoARG(val)}\nDolar Australiano: ${dolarAUS(val)}\nDólar Canadense: $ {dolarCAN(val)}\nFranco Suiço: ${francoSUI(val)}\nEuro: ${euro(val)}\nLibra Esterlina {libra(val)}")