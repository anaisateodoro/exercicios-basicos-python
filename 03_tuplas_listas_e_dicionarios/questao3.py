"""3)Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra."""

carrinho = {}
precos = {
    'Sabonete em barra': 3, 
    'Creme dental': 20, 
    'Escova dental': 5}

# Adicionar produtos ao carrinho
carrinho['Sabonete em barra'] = carrinho.get('Sabonete em barra', 0) + 2
carrinho['Creme dental'] = carrinho.get('Creme dental', 0) + 1
carrinho['Escova dental'] = carrinho.get('Escova dental', 0) + 3

# Calcular o total do carrinho
total = 0
for produto, quantidade in carrinho.items():
    preco = precos.get(produto, 0)
    total += preco * quantidade

# Exibir resultados
print('Carrinho:', carrinho)
print('Total: R$', total)
