class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print(f"Subindo para o andar {self.atualAndar}. Pessoas no elevador: {self.atualCapacidade}")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print(f"Descendo para o andar {self.atualAndar}. Pessoas no elevador: {self.atualCapacidade}")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self, num_pessoas):
        if self.atualCapacidade + num_pessoas <= self.totalCapacidade:
            self.atualCapacidade += num_pessoas
            print(f"Entrando {num_pessoas} pessoa(s). Pessoas no elevador: {self.atualCapacidade}")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def sair(self, num_pessoas):
        if self.atualCapacidade - num_pessoas >= 0:
            self.atualCapacidade -= num_pessoas
            print(f"Saindo {num_pessoas} pessoa(s). Pessoas no elevador: {self.atualCapacidade}")
        else:
            print("NÃO TEM NINGUÉM")

# Exemplo de uso
elevador = Elevador(totalCapacidade=7, totalAndar=10)

elevador.subir()
elevador.entrar(2)
elevador.subir()
elevador.entrar(3)
elevador.sair(1)
elevador.descer()
elevador.descer()
