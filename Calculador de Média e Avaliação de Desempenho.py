def calcular_media(notas):
    total_notas = len(notas)
    
    if total_notas == 0:
        return 0
    
    soma_notas = sum(notas)
    media = soma_notas / total_notas
    return media

def avaliar_desempenho(media):
    if media >= 7:
        return "Desempenho excelente!"
    elif media >= 5:
        return "Desempenho satisfatório."
    else:
        return "Desempenho insatisfatório. É recomendável buscar melhorias."

def main():
    print("Bem-vindo ao Calculador de Média!")
    
    try:
        num_notas = int(input("Quantas notas você deseja inserir?: "))
    except ValueError:
        print("Por favor, insira um número válido para a quantidade de notas.")
        return

    notas = []
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Informe a nota {i + 1}: "))
                break
            except ValueError:
                print("Ops..., Isto não é um número. Tente novamente.")

        notas.append(nota)
    
    media = calcular_media(notas)
    
    print(f"A média das notas é: {media:.2f}")
    
    feedback = avaliar_desempenho(media)
    print(feedback)

if __name__ == "__main__":
    main()
