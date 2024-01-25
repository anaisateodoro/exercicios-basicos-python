def contar_vogais(frase):
    total_vogais = 0 
    vogais = "aeiouAEIOU"    
    for char in frase:       
        if char in vogais:
            total_vogais += 1    
    return total_vogais
frase_usuario = input("Digite uma frase: ")
resultado = contar_vogais(frase_usuario)
print(f"A frase '{frase_usuario}' possui {resultado} vogais.")