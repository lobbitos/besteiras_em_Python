tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]
turno = 9
vez = 0
jogador1 = 0
jogador2 = 0

print("-------Jogo da Velha-------")
print(f"         {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
print("        ---+---+---")
print(f"         {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
print("        ---+---+---")
print(f"         {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
print("Escolha o nº da casa para jogar\n")

while turno > vez:
    if vez % 2 == 0:
        print("--- JOGADOR (X) ---")
        escolha = int(input("Digite o número "))
        if tabuleiro[escolha] == "O" or tabuleiro[escolha] == "X":
            print("Casa já jogada tente novamente!")
            continue
        if escolha in tabuleiro:
            tabuleiro[escolha] = "X"
            vez += 1
            jogador1 += escolha
        else:
            print("Escolha invalida! Digite novamente.")
            continue

        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n ")

    else:
        print("--- JOGADOR (O) ---")
        escolha = int(input("Digite o número "))
        if tabuleiro[escolha] == "X" or tabuleiro[escolha] == "O":
            print("Casa já jogada tente novamente!")
            continue
        if escolha in tabuleiro:
            tabuleiro[escolha] = "O"
            vez += 1
            jogador2 += escolha
        else:
            print("Escolha invalida! Digite novamente.")
            continue

        print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n ")

    # Condições de vitória X:
    if tabuleiro[0] == "X" and tabuleiro[1] == "X" and tabuleiro[2] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[3] == "X" and tabuleiro[4] == "X" and tabuleiro[5] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[6] == "X" and tabuleiro[7] == "X" and tabuleiro[8] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[0] == "X" and tabuleiro[4] == "X" and tabuleiro[8] == "X":
        print("\tX GANHOU")
        break
    if tabuleiro[2] == "X" and tabuleiro[4] == "X" and tabuleiro[6] == "X":
        print("\t X GANHOU")
        break

    # Condições de vitória O:
    if tabuleiro[0] == "O" and tabuleiro[1] == "O" and tabuleiro[2] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[3] == "O" and tabuleiro[4] == "O" and tabuleiro[5] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[6] == "O" and tabuleiro[7] == "O" and tabuleiro[8] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[0] == "O" and tabuleiro[3] == "O" and tabuleiro[6] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[1] == "O" and tabuleiro[4] == "O" and tabuleiro[7] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[2] == "O" and tabuleiro[5] == "O" and tabuleiro[8] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[0] == "O" and tabuleiro[4] == "O" and tabuleiro[8] == "O":
        print("\tO GANHOU")
        break
    if tabuleiro[2] == "O" and tabuleiro[4] == "O" and tabuleiro[6] == "O":
        print("\t O GANHOU")
        break
print(f"\t {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
print("\t---+---+---")
print(f"\t {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
print("\t---+---+---")
print(f"\t {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n ")

print("\tFIM\n\tObrigado por jogar!\n")
