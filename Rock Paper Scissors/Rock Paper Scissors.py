import random


print("""
               WELCOME TO MY GAME:   
            "Rock – Paper – Scissors"

""")


rock = "Rock"
paper = "Paper"
scissors = "Scissors"


rock_list = ["r", "rock"]
paper_list = ["p", "paper"]
scissors_list = ["s", "scissors"]


count_player_wins = 0
count_computer_wins = 0


yes_list = ["y", "yes"]
no_list = ["n", "no"]


while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()

    if player_move in rock_list:
        player_move = rock

    elif player_move in paper_list:
        player_move = paper

    elif player_move in scissors_list:
        player_move = scissors

    else:
        print("Invalid Input. Try again...\n\n")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock

    elif computer_random_number == 2:
        computer_move = paper

    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer choose {computer_move}.")

    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        count_player_wins += 1

        print("\n            You win!")
        print(f"\nPlayer -> {count_player_wins} wins : Computer -> {count_computer_wins} wins\n\n")

    elif player_move == computer_move:
        print("\n            Draw!\n")
        continue

    else:
        count_computer_wins += 1

        print("\n            You lose!")
        print(f"\nPlayer -> {count_player_wins} wins : Computer -> {count_computer_wins} wins\n\n")

    command = input("Type [yes] to Play Again or [no] to quit: ").lower()
    if command in yes_list:
        print("\n")
        continue

    elif command in no_list:
        print("""

             !THANK YOU FOR PLAYING!
        """)
        break

    else:
        raise SystemExit("Invalid command! Try again...")
