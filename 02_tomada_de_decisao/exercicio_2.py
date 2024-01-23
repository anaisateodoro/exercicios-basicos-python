

def saudacao_turno():
    while True:
        turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ").upper()
    
        if turno == "M":
            print("Bom Dia!")
        elif turno == "V":
            print("Boa Tarde!")
        elif turno == "N":
            print("Boa Noite!")
        else:
            print("Valor Inválido!")

saudacao_turno()