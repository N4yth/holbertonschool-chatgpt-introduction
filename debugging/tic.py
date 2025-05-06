#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Veuillez entrer un nombre entre 0 et 2.")
            continue

        value = int(value)
        if 0 <= value <= 2:
            return value
        else:
            print("Nombre invalide. Il doit être entre 0 et 2.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"Tour du joueur {player}")
        
        row = get_valid_input("Entrez l'indice de la ligne (0, 1, ou 2) : ")
        col = get_valid_input("Entrez l'indice de la colonne (0, 1, ou 2) : ")

        if board[row][col] != " ":
            print("Cette case est déjà occupée. Choisissez une autre.")
            continue

        board[row][col] = player
        moves += 1

        if check_winner(board):
            print_board(board)
            print(f"Le joueur {player} a gagné !")
            break

        if moves == 9:
            print_board(board)
            print("Match nul !")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()