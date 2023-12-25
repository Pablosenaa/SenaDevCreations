class Produto:
    def __init__(self, nome, quantidade, valor_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.atualizar_total()

    def atualizar_total(self):
        self.total = self.quantidade * self.valor_unitario

class ListaDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                return True
        return False

    def atualizar_produto(self, nome, nova_quantidade, novo_valor_unitario):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.quantidade = nova_quantidade
                produto.valor_unitario = novo_valor_unitario
                produto.atualizar_total()
                return True
        return False

    def calcular_total(self):
        return sum(produto.total for produto in self.produtos)

    def exibir_lista(self):
        if not self.produtos:
            print("A lista de compras está vazia.")
        else:
            print("\nLista de Compras:")
            for produto in self.produtos:
                print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Valor Unitário: R${produto.valor_unitario:.2f}, Total: R${produto.total:.2f}")
            print(f"\nValor Total da Lista: R${self.calcular_total():.2f}")

def menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar Produto")
    print("2. Ver Lista de Produtos")
    print("3. Atualizar Produto")
    print("4. Remover Produto")
    print("5. Encerrar Programa")

if __name__ == "__main__":
    lista_compras = ListaDeCompras()

    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            while True:
                quantidade_input = input("Digite a quantidade do produto: ")
                if quantidade_input.isdigit():
                    quantidade = int(quantidade_input)
                    break
                else:
                    print("Ops..., Isto não é um número. Tente novamente.")

            while True:
                valor_input = input("Digite o valor unitário do produto: ")
                valor_input = valor_input.replace(',', '.')  # Substitui vírgula por ponto
                try:
                    valor_unitario = float(valor_input)
                    break
                except ValueError:
                    print("Ops..., Isto não é um número. Tente novamente.")

            novo_produto = Produto(nome, quantidade, valor_unitario)
            lista_compras.adicionar_produto(novo_produto)
            print(f"{nome} adicionado à lista.")

        elif opcao == '2':
            lista_compras.exibir_lista()

        elif opcao == '3':
            nome = input("Digite o nome do produto a ser atualizado: ")
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            novo_valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            if lista_compras.atualizar_produto(nome, nova_quantidade, novo_valor_unitario):
                print(f"{nome} atualizado com sucesso.")
            else:
                print(f"{nome} não encontrado na lista.")

        elif opcao == '4':
            nome = input("Digite o nome do produto a ser removido: ")
            if lista_compras.remover_produto(nome):
                print(f"{nome} removido da lista.")
            else:
                print(f"{nome} não encontrado na lista.")

        elif opcao == '5':
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
