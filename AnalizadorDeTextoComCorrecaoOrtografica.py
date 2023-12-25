from spellchecker import SpellChecker

def corrigir_palavras(texto):
    spell = SpellChecker()
    palavras = texto.split()

    # Identificar palavras incorretas
    palavras_incorretas = spell.unknown(palavras)

    # Corrigir palavras incorretas
    for palavra_incorreta in palavras_incorretas:
        correcao = spell.correction(palavra_incorreta)
        texto = texto.replace(palavra_incorreta, correcao)

    return texto

def analisar_texto(texto):
    # Remover caracteres especiais e converter para minúsculas
    texto = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in texto)

    # Corrigir palavras incorretas
    texto_corrigido = corrigir_palavras(texto)

    # Contar o número de palavras
    palavras = texto_corrigido.split()
    numero_palavras = len(palavras)

    # Contar o número de letras
    numero_letras = sum(c.isalpha() for c in texto_corrigido)

    return numero_palavras, numero_letras, texto_corrigido

def main():
    print("Bem-vindo ao Analisador de Texto com Correção Ortográfica!")
    texto = input("Digite o texto que deseja analisar: ")

    # Chamar a função de análise
    palavras, letras, texto_corrigido = analisar_texto(texto)

    print(f"\nTexto corrigido: {texto_corrigido}")
    print(f"Número de palavras: {palavras}")
    print(f"Número de letras: {letras}")

if __name__ == "__main__":
    main()
