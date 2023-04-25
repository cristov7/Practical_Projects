import random


class SlotMachine:
    def __init__(self):
        self.icons: list = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓']
        self.bet: int = 0
        self.balance: int = 0

    def add_money(self, amount: int) -> str:
        self.balance += amount
        return f"\n\nAdded {amount} lv. to your balance." \
               f"\nYour new balance is: {self.balance} lv."

    def remove_money(self, amount: int) -> str:
        if amount <= self.balance:
            self.balance -= amount
            return f"\n\nRemoved {amount} lv.from your balance." \
                   f"\nYour new balance is: {self.balance}"

        else:
            return f"\n\nCan't remove {amount} lv. from your balance!" \
                   f"\nYour balance is: {self.balance}"

    def play(self) -> str:
        if self.balance <= 0:
            return "Sorry, you don't have enough money to play."

        else:
            while True:
                try:
                    self.bet = int(input("\n\nEnter your bet: "))
                    if self.bet <= 0 or self.bet > self.balance:
                        raise ValueError
                    else:
                        break

                except ValueError:
                    print("Invalid bet. Please enter a number between 1 and", self.balance)

            count_icon_per_reel = 5
            reels_list = [random.choice(self.icons)
                          for icon in range(count_icon_per_reel)]
            print("\n")
            print(" ".join(reels_list))

            if len(set(reels_list)) == 1:   # 5 equal icons
                winnings = self.bet * 10
                print(f"!!!!! JACKPOT !!!!!"
                      f"\nYou won {winnings} lv!")

            elif len(set(reels_list)) == 2:   # 4 equal icons
                winnings = self.bet * 5
                print(f"!!! BIG WIN !!!"
                      f"\nYou won {winnings} lv!")

            elif len(set(reels_list)) == 3:   # 3 equal icons
                winnings = self.bet * 2
                print(f"! CONGRATULATIONS !"
                      f"\nYou won {winnings} lv!")

            elif len(set(reels_list)) == 4:   # 2 equal icons
                winnings = 0
                print("Sorry, you didn't win this time...")

            else:   # all icons are different
                winnings = 0
                print("Sorry, you didn't win this time...")

            self.balance += winnings - self.bet
            return f"Your balance is now {self.balance} lv."


# print("\n\n--- Welcome to MAGIC CASINO ---\n\n")
#
#
# start_list = ["START", "S"]
# exit_list = ["EXIT", "E"]
# add_list = ["ADD", "A"]
#
#
# money_amount = int(input("Please insert money: "))
#
#
# player = SlotMachine()
# print(player.add_money(money_amount))
#
#
# while True:
#     option = input("\n\nOptions:"
#                    "\n - Press -> [S]tart the game: "
#                    "\n - Press -> [E]xit the game: "
#                    "\n - Press -> [A]dd more money: "
#                    "\nChoose: ").upper()
#
#     if option in start_list:
#         print(player.play())
#
#     elif option in exit_list:
#         balance = player.balance
#         print(player.remove_money(balance))
#
#         print("\n\n    Thank you for playing!\n\n")
#         break
#
#     elif option.upper() in add_list:
#         money_amount = int(input("\n\nPlease insert money: "))
#         print(player.add_money(money_amount))
#
#     else:
#         print("\n\nInvalid options!"
#               "\nPlease, try again!")
