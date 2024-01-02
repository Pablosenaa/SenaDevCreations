class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor/Editora: {self.autor_ou_editora}")


class Livro(Material):
    def __init__(self, titulo, autor, genero, num_paginas):
        super().__init__(titulo, autor)
        self.genero = genero
        self.num_paginas = num_paginas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Gênero: {self.genero}")
        print(f"Número de Páginas: {self.num_paginas}")


class Revista(Material):
    def __init__(self, titulo, editora, edicao, periodicidade):
        super().__init__(titulo, editora)
        self.edicao = edicao
        self.periodicidade = periodicidade

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Edição: {self.edicao}")
        print(f"Periodicidade: {self.periodicidade}")


# Exemplo de uso
livro = Livro("Dom Casmurro", "Machado de Assis", "Romance", 300)
revista = Revista("National Geographic", "Editora Abril", "Julho 2022", "Mensal")

print("Detalhes do Livro:")
livro.exibir_informacoes()

print("\nDetalhes da Revista:")
revista.exibir_informacoes()
