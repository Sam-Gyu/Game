# File name: CS112_A1_T2_game number(3)_20231076.py.
# Name: Sama Waleed Mohammed
# Program: Sabtract square numbers game
# Purpose: This is a two-player mathematical game of strategy. It is played by two people with a pile of coins. The players take turns removing coins from the pile, always removing a non-zero square number of coins (1, 4, 9, 16, …). The player who removes the last coin wins.

def IsTheNumSquare(num):
    # Function to check if the move is a square number or not
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

print("Welcome to the subtract game")
choose = input('A) Do you want me to choose a number for you\nB) Do you want to choose a number by yourself\n')
if choose == 'A':
    coins = 200
else:
    coins = int(input('Enter the number of coins here:'))

while coins > 0:
    print("Current number of coins:", coins)

    # player 1
    while True:
        try:
            move = int(input("Player 1: Enter a square number: "))
            if move > coins:
                print('The number you choose is greater than the number of coins')
            elif move == 0:
                print('Invalid number')
            elif IsTheNumSquare(move):
                coins -= move
                break
            else:
                print("Invalid number")
        except ValueError:
            print("Invalid input")

    if coins == 0:
        print("Player one is the winner")
        break
    print("The coins we have now are", coins)

    # player 2
    while True:
        try:
            move = int(input("Player 2: Enter a square number: "))
            if move > coins:
                print('The number you choose is greater than the number of coins')
            elif move == 0:
                print('Invalid number')
            elif IsTheNumSquare(move):
                coins -= move
                break
            else:
                print("Invalid number")
        except ValueError:
            print("Invalid input")

    if coins == 0:
        print("Player Two is the winner")
        break




