"""4) Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome."""

contatos = {
    'Dhu':'98765-4321',
    'Edyr':'98456-7890',
    'Leiloca':'93467-8912',
    'Lidoka':'95678-9123',
    'Regina':'95679-0234',
    'Sandra':'96778-2345'
    }

nome_procurado = input('Digite o nome que deseja consultar na lista de contatos do grupo das Frenéticas: ')

if nome_procurado in contatos:
    telefone = contatos[nome_procurado]
    print(f'O número de telefone de {nome_procurado} é {telefone} .')
else:
    print(f'Desculpe, o contato {nome_procurado} não consta na lista de contatos do grupo das Frenéticas.')

