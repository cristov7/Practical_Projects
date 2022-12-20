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
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move.lower() in rock_list:
        player_move = rock
    elif player_move.lower() in paper_list:
        player_move = paper
    elif player_move.lower() in scissors_list:
        player_move = scissors
    else:
        # print("Invalid Input. Try again...")
        # break
        raise SystemExit("Invalid Input. Try again...")
    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    # elif computer_random_number == 3:
    else:
        computer_move = scissors
    print(f"The computer choose {computer_move}.")
    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        print("You win!")
        count_player_wins += 1
        print(f"\n\nPlayer -> {count_player_wins} wins : Computer -> {count_computer_wins} wins\n\n")
    elif player_move == computer_move:
        print("Draw!")
        continue
    else:
        print("You lose!")
        count_computer_wins += 1
        print(f"\n\nPlayer -> {count_player_wins} wins : Computer -> {count_computer_wins} wins\n\n")
    command = input("Type [yes] to Play Again or [no] to quit: ")
    if command.lower() in yes_list:
        continue
    elif command.lower() in no_list:
        print("""

                THANK YOU FOR PLAYING!
        """)
        break
    else:
        raise SystemExit("Invalid Input. Try again...")
        # print("Invalid Input. Try again...")
        # break
