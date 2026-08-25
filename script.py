# ==========================================
# JOVI STUDY MODE
# Sistema de organização de fotos para estudos
# ==========================================

def exibir_menu():
    """Exibe o menu principal e retorna a opção escolhida."""
    print("\n====== JOVI STUDY MODE ======")
    print("1 - Adicionar foto")
    print("2 - Ver galeria")
    print("3 - Identificar matéria")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def adicionar_foto(lista_fotos):
    """Adiciona uma nova foto com validação de entrada."""
    nome_foto = input("\nDigite o nome da foto: ")

    # Validação rigorosa da matéria (o loop só quebra se digitar certo)
    materia = ""
    while True:
        print("\nEscolha a matéria:")
        print("1 - Matemática")
        print("2 - História")
        print("3 - Biologia")
        print("4 - Física")
        escolha = input("Digite a opção (1-4): ")

        if escolha == "1":
            materia = "Matemática"
            break
        elif escolha == "2":
            materia = "História"
            break
        elif escolha == "3":
            materia = "Biologia"
            break
        elif escolha == "4":
            materia = "Física"
            break
        else:
            print("Opção inválida! Por favor, digite um número de 1 a 4.")

    # Criando o dicionário e adicionando à lista
    foto = {
        "nome": nome_foto,
        "materia": materia
    }
    lista_fotos.append(foto)
    print(f"\nFoto '{nome_foto}' salva com sucesso na matéria de {materia}!")

def ver_galeria(lista_fotos):
    """Exibe todas as fotos armazenadas na lista."""
    if len(lista_fotos) == 0:
        print("\nNenhuma foto cadastrada no momento.")
        return # Retorna prematuramente se a lista estiver vazia

    print("\n====== GALERIA ======")
    for foto in lista_fotos:
        print(f"Foto: {foto['nome']}")
        print(f"Matéria: {foto['materia']}")
        print("----------------------")

def identificar_materia():
    """Analisa o texto e identifica a matéria correspondente."""
    texto = input("\nDigite um texto da imagem: ").lower()

    if "equação" in texto or "raiz" in texto:
        print("-> Matéria identificada: Matemática")
    elif "revolução" in texto or "império" in texto:
        print("-> Matéria identificada: História")
    elif "célula" in texto or "dna" in texto:
        print("-> Matéria identificada: Biologia")
    elif "força" in texto or "velocidade" in texto:
        print("-> Matéria identificada: Física")
    else:
        print("-> Matéria não identificada. Tente inserir mais palavras-chave.")

def main():
    """Função principal que controla o fluxo do programa."""
    fotos = [] # Lista principal de dicionários
    continuar = True

    while continuar:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_foto(fotos)
        elif opcao == "2":
            ver_galeria(fotos)
        elif opcao == "3":
            identificar_materia()
        elif opcao == "4":
            print("\nEncerrando sistema... Até logo!")
            continuar = False
        else:
            print("\nOpção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()