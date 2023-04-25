import random


class Game:
    def __init__(self, max_attempts: int = 3):
        self.max_attempts = max_attempts
        self.number: int = random.randint(1, 10)
        self.attempts: int = 0
        self.won: bool = False

    def guess(self, number) -> None:
        self.attempts += 1

        if number > self.number:
            print(f"The number is lower than your number!\n")

        elif number < self.number:
            print(f"The number is higher than your number!\n")

        elif number == self.number:
            self.won = True

            print("\n\n        Congratulations!"
                  "\n            You won!\n")

        if self.attempts == self.max_attempts and not self.won:
            print(f"\n        Sorry, you lost!"
                  f"\n        The number is {self.number}!\n")


# print("""
#         Guess the number
#
# """)
#
#
# game = Game()
#
#
# while True:
#     if game.won or game.attempts == game.max_attempts:
#         break
#
#     else:
#         current_number = int(input("Guess a number between 1 to 10: "))
#         game.guess(current_number)
