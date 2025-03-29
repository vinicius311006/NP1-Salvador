import os

# Função que exibe o menu principal
def menu():
    os.system('cls')  # Limpa a tela
    print("\nMenu Principal:")
    print("(1) - Aprender")  # Opção para aprender sobre comandos
    print("(2) - Fazer um Quiz")  # Opção para fazer o quiz
    print("(3) - Sair")  # Opção para sair do programa
    
# Função para o modo de aprendizado
def aprender():
    while True:  # Loop para garantir que o usuário só saia do modo aprender quando escolher a opção "5"
        os.system('cls')  # Limpa a tela
        print("\nModo Aprender:")
        print("(1) - Como exibir mensagens na tela?")  # Explicação sobre o comando print()
        print("(2) - Como receber dados do usuário?")  # Explicação sobre o comando input()
        print("(3) - Quem é o criador da linguagem Python?")  # Explicação sobre o criador do Python
        print("(4) - Quando o Python foi lançado?")  # Explicação sobre o lançamento do Python
        print("(5) - Voltar ao menu principal")  # Opção para voltar ao menu principal
        opcao = input("Escolha uma opção: ")  # Pergunta para o usuário escolher a opção

        # Se o usuário escolheu a opção 1, mostra a explicação sobre o comando print()
        if opcao == '1':
            os.system('cls')  # Limpa a tela
            print("\nExplicação sobre o comando print():")
            print("🟥 O comando print() é utilizado para exibir mensagens na tela do usuário.")
            print('⬜ Exemplo: print("Olá, Mundo!")')
            print("⬜ Este comando exibe a mensagem 'Olá, Mundo!' na tela.")
            os.system('pause')

            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")  # Pergunta se quer fazer o quiz
            if fazer_quiz.lower() == "s":  # Se o usuário respondeu "s", chama a função do quiz
                quiz()

        # Se o usuário escolheu a opção 2, mostra a explicação sobre o comando input()
        elif opcao == '2':
            print("\nExplicação sobre o comando input():")
            print("🟥 O comando input() é utilizado para receber dados do usuário.")
            print('⬜ Exemplo: nome = input("Qual é o seu nome? ")')
            print("⬜ Este comando solicita que o usuário digite seu nome, e armazena a resposta na variável 'nome'.")
            os.system('pause')

            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")  # Pergunta se quer fazer o quiz
            if fazer_quiz.lower() == 's':  # Se o usuário respondeu "s", chama a função do quiz
                quiz()

        # Se o usuário escolheu a opção 3, mostra a explicação sobre o criador do Python
        elif opcao == '3':
            os.system('cls')  # Limpa a tela
            print("\nExplicação sobre o criador do Python:")
            print("🟥 A linguagem Python foi criada por Guido van Rossum, um programador holandês.")
            print("⬜ Ele iniciou o projeto em 1980 e a primeira versão foi lançada em 1991.")
            os.system('pause')

            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")  # Pergunta se quer fazer o quiz
            if fazer_quiz.lower() == 's':  # Se o usuário respondeu "s", chama a função do quiz
                quiz()

        # Se o usuário escolheu a opção 4, mostra a explicação sobre o lançamento do Python
        elif opcao == '4':
            os.system('cls')  # Limpa a tela
            print("\nExplicação sobre o lançamento do Python:")
            print("🟥 Python foi lançado oficialmente em 1991 por Guido van Rossum. ")
            print("⬜ A linguagem foi projetada para ser simples e fácil de ler, com foco em legibilidade de código.")
            os.system('pause')

            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")  # Pergunta se quer fazer o quiz
            if fazer_quiz.lower() == 's':  # Se o usuário respondeu "s", chama a função do quiz
                quiz()

        # Se o usuário escolheu a opção 5, simplesmente retorna ao menu
        elif opcao == '5':
            return
        else:
            print("Opção inválida. Tente novamente.")  # Se o usuário escolheu uma opção inválida

# Função do quiz, onde o usuário vai responder as perguntas
def quiz():
    os.system('cls')  # Limpa a tela
    print("\nQuiz - Teste seus conhecimentos!")
    acertos = 0  # Inicializa o contador de acertos

    # Pergunta 1
    resposta = input("1. Como exibir uma mensagem na tela em Python? \n(a) input() \n(b) print() \n(c) echo() \n(d) show() \nEscolha a opção (a/b/c/d): ")
    if resposta.lower() == 'b':  # Se a resposta for a alternativa correta "b"
        print("Correto!")
        acertos += 1  # Incrementa o contador de acertos
    else:
        print("Errado. A resposta correta é: (b) print()")
    

    # Pergunta 2
    os.system('cls')  # Limpa a tela
    resposta = input("2. Como receber dados do usuário em Python? \n(a) input() \n(b) print() \n(c) read() \n(d) get() \nEscolha a opção (a/b/c/d): ")
    if resposta.lower() == 'a':  # Se a resposta for a alternativa correta "a"
        print("Correto!")
        acertos += 1  # Incrementa o contador de acertos
    else:
        print("Errado. A resposta correta é: (a) input()")
    

    # Pergunta 3: Quem é o criador da linguagem Python?
    os.system('cls')  # Limpa a tela
    resposta = input("3. Quem é o criador da linguagem Python? \n(a) Steve Jobs \n(b) Bill Gates \n(c) Guido van Rossum \n(d) Mark Zuckerberg \nEscolha a opção (a/b/c/d): ")
    if resposta.lower() == 'c':  # Se a resposta for a alternativa correta "c"
        print("Correto!")
        acertos += 1  # Incrementa o contador de acertos
    else:
        print("Errado. A resposta correta é: (c) Guido van Rossum")
    

    # Pergunta 4: Quando o Python foi lançado?
    os.system('cls')  # Limpa a tela
    resposta = input("4. Quando o Python foi lançado? \n(a) 1980 \n(b) 1991 \n(c) 2000 \n(d) 2005 \nEscolha a opção (a/b/c/d): ")
    if resposta.lower() == 'b':  # Se a resposta for a alternativa correta "b"
        print("Correto!")
        acertos += 1  # Incrementa o contador de acertos
    else:
        print("Errado. A resposta correta é: (b) 1991")
    

    # Exibe o total de acertos no quiz
    os.system('cls')  # Limpa a tela
    print(f"\nVocê acertou {acertos} de 4 questões.")
    
    # Aguarda o usuário pressionar uma tecla para retornar ao menu
    print("Precione Qualquer Tecla: ")
    os.system('pause')

# Loop principal do programa, que fica executando até o usuário escolher sair
while True:
    menu()  # Chama a função para exibir o menu
    opcao = input("Escolha uma opção: ")  # Pergunta ao usuário qual opção escolher

    if opcao == '1':
        aprender()  # Se o usuário escolher "1", chama a função de aprendizado
    elif opcao == '2':
        quiz()  # Se o usuário escolher "2", chama a função do quiz
    elif opcao == '3':
        print("Saindo... Até logo!")  # Se o usuário escolher "3", encerra o programa
        break  # Sai do loop e termina o programa
    else:
        print("Opção inválida. Tente novamente.")  # Se o usuário escolher uma opção inválida
