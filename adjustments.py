import numpy as np
import random

MAX_POSITION = 100
DICE_MIN = 2
DICE_MAX = 12
BOARD_SIZE = 10
DEFAULT_MARKER = '_'
PLAYER1_MARKER = 'X'
PLAYER2_MARKER = 'Y'

def print_arrays_with_borders(array1, array2):
    for row1, row2 in zip(array1, array2):
        row_str = '|'
        for elem1, elem2 in zip(row1, row2):
            row_str += f"{elem1}{elem2}||"
        print(row_str[:-1])

def update_player_position(board, position, marker):
    board.fill(DEFAULT_MARKER)
    if position >= MAX_POSITION:
        board[BOARD_SIZE - 1, BOARD_SIZE - 1] = marker
    elif position < 10:
        board[0, position - 1] = marker
    elif position % 10 == 0:
        board[position // 10 - 1, BOARD_SIZE - 1] = marker
    else:
        board[position // 10, position % 10 - 1] = marker
    return board

def handle_money_change(money, dice_roll):
    outcome = random.randint(1, 3)
    if outcome == 1:
        change = -100 * dice_roll
    elif outcome == 2:
        change = 200 * dice_roll
    else:
        change = 50 * dice_roll

    money += change
    print(f"You {'win' if change > 0 else 'lose'} ${abs(change)}\n")
    return money

def display_instructions():
    print("Instructions:")
    print("1. Each player rolls a pair of dice to move forward.")
    print("2. The amount of money changes based on the dice roll.")
    print("3. The goal is to reach the end with the most money.")

def main():
    user_input = input("Press 'q' to quit, 'i' for instructions, or any other key to continue: ").lower()
    if user_input == 'q':
        print("Exiting the game.")
        return
    elif user_input == 'i':
        display_instructions()

    player_positions = [0, 0]
    player_money = [0, 0]
    player_boards = [np.full((BOARD_SIZE, BOARD_SIZE), DEFAULT_MARKER, dtype=str) for _ in range(2)]
    players_finished = [False, False]

    while not all(players_finished):
        for i in range(2):
            if not players_finished[i]:
                input(f"Player {i + 1}, press any key to roll a pair of dice: ")
                dice_roll = random.randint(DICE_MIN, DICE_MAX)
                print(f"You rolled {dice_roll}!")
                player_positions[i] = min(player_positions[i] + dice_roll, MAX_POSITION)
                player_boards[i] = update_player_position(player_boards[i], player_positions[i], PLAYER1_MARKER if i == 0 else PLAYER2_MARKER)
                print_arrays_with_borders(*player_boards)
                player_money[i] = handle_money_change(player_money[i], dice_roll)
                print(f"Player 1: ${player_money[0]}")
                print(f"Player 2: ${player_money[1]}\n")
                if player_positions[i] >= MAX_POSITION:
                    print(f"Player {i + 1} has finished the game!")
                    players_finished[i] = True

    if player_money[0] == player_money[1]:
        print("It's a tie!")
    else:
        winner = "Player 1" if player_money[0] > player_money[1] else "Player 2"
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()