import random


print("""
            WELCOME TO MY GAME:
             "GUESS A NUMBER"

""")


computer_number = random.randint(1, 100)
count_attempts = 0


yes_list = ["y", "yes"]
no_list = ["n", "no"]


while True:
    player_number = input("Guess the number (1-100): ")

    if not player_number.isdigit():
        print("Invalid input. Try again...\n\n")

    else:
        player_number = int(player_number)
        count_attempts += 1

        if player_number == computer_number:
            print(f"Number of attempts: {count_attempts}\nYou guess it!")
            print("""
             
             CONGRATULATIONS!
             
            """)

            command = input("Type [yes] to Play Again or [no] to quit: ").lower()
            if command in yes_list:
                continue

            elif command in no_list:
                print("""
                
             THANK YOU FOR PLAYING!
                """)
                break

            else:
                raise SystemExit("Invalid Input. Try again...")

        elif player_number > computer_number:
            print(f"Number of attempts: {count_attempts} -> Too High!\n\n")

        elif player_number < computer_number:
            print(f"Number of attempts: {count_attempts} -> Too Low!\n\n")
