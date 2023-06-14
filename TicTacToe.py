def exibir_tabuleiro(tabuleiro):
    print("-------------")
    for linha in tabuleiro:
        print("|", end=" ")
        for celula in linha:
            print(celula, end=" | ")
        print("\n-------------")


def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False


def jogar():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0, 1, 2): "))
        coluna = int(input("Digite o número da coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            print("Parabéns! Jogador", jogador_atual, "venceu!")
            break

        if all(all(celula != " " for celula in linha) for linha in tabuleiro):
            print("O jogo empatou!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


jogar()