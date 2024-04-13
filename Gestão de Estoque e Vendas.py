produtos = {
    1: ["Arroz 1Kg", 3.99, 220, 22, False],
    2: ["Feijão 2Kg", 8.99, 120, 12, False],
    3: ["Biscoito ABC", 2.75, 30, 30, True]
}

def menu():
    print("------- Menu Principal -------")
    print("1 - Listar produtos")
    print("2 - Cadastrar produto")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("5 - Realizar compra")
    print("6 - Relatórios")
    print("0 - Sair")
    print("-----------------------------")

def menu_relatorios():
    print("------- Submenu de Relatórios -------")
    print("1 - Relatório de estoque mínimo")
    print("2 - Relatório de produtos em estoque")
    print("3 - Relatório de produtos vendidos")
    print("0 - Voltar ao menu principal")
    print("-------------------------------------")

def listar_produtos():
    print("------- Produtos cadastrados -------")
    for chave, produto in produtos.items():
        print(f"ID: {chave}")
        print(f"Descrição: {produto[0]}")
        print(f"Preço: R${produto[1]}")
        print(f"Quantidade em estoque: {produto[2]}")
        print(f"Quantidade mínima em estoque: {produto[3]}")
        print(f"Estoque mínimo atingido: {'Sim' if produto[4] else 'Não'}")
        print("-----------------------------------")

def cadastrar_produto():
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))
    estoque_minimo_atingido = False
    
    if quantidade <= quantidade_minima:
        estoque_minimo_atingido = True
        
    novo_id = max(produtos.keys()) + 1 if produtos else 1
    produtos[novo_id] = [descricao, preco, quantidade, quantidade_minima, estoque_minimo_atingido]
    print("Produto cadastrado com sucesso!")

def atualizar_produto():
    listar_produtos()
    produto_id = int(input("Digite o ID do produto que deseja atualizar: "))
    
    if produto_id in produtos:
        descricao = input("Digite a nova descrição do produto: ")
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        quantidade_minima = int(input("Digite a nova quantidade mínima em estoque: "))
        estoque_minimo_atingido = False
        
        if quantidade <= quantidade_minima:
            estoque_minimo_atingido = True
            
        produtos[produto_id] = [descricao, preco, quantidade, quantidade_minima, estoque_minimo_atingido]
        print("Produto atualizado com sucesso!")
    else:
        print("ID do produto não encontrado.")

def excluir_produto():
    listar_produtos()
    produto_id = int(input("Digite o ID do produto que deseja excluir: "))
    
    if produto_id in produtos:
        confirmacao = input("Tem certeza que deseja excluir este produto? (s/n): ")
        
        if confirmacao.lower() == "s":
            del produtos[produto_id]
            print("Produto excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("ID do produto não encontrado.")

def realizar_compra():
    listar_produtos()
    produto_id = int(input("Digite o ID do produto que deseja comprar: "))
    
    if produto_id in produtos:
        quantidade_comprada = int(input("Digite a quantidade que deseja comprar: "))
        
        if quantidade_comprada > produtos[produto_id][2]:
            print("Quantidade insuficiente em estoque.")
        else:
            produtos[produto_id][2] -= quantidade_comprada
            print(f"Compra realizada com sucesso. Total: R${produtos[produto_id][1] * quantidade_comprada}")
            if produtos[produto_id][2] <= produtos[produto_id][3]:
                produtos[produto_id][4] = True
    else:
        print("ID do produto não encontrado.")

# Loop principal
while True:
    menu()
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        cadastrar_produto()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        excluir_produto()
    elif opcao == "5":
        realizar_compra()
    elif opcao == "6":
        while True:
            menu_relatorios()
            opcao_relatorios = input("Digite a opção desejada: ")
            
            if opcao_relatorios == "1":
                # Função para gerar relatório de estoque mínimo
                pass
            elif opcao_relatorios == "2":
                # Função para gerar relatório de produtos em estoque
                pass
            elif opcao_relatorios == "3":
                # Função para gerar relatório de produtos vendidos
                pass
            elif opcao_relatorios == "0":
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida. Por favor, tente novamente.")

print("Programa encerrado.")