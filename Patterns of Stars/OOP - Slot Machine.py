import random


class SlotMachine:
    def __init__(self):
        self.icons = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓']
        self.bet = 0
        self.balance = 0

    def add_money(self, amount: int) -> None:
        self.balance += amount
        print(f"\n\nAdded {amount} lv. to your balance."
              f"\nYour new balance is: {self.balance} lv.")

    def remove_money(self, amount: int) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"\n\nRemoved {amount} lv.from your balance."
                  f"\nYour new balance is: {self.balance}")

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


player = SlotMachine()
print("\n\n--- Welcome to MAGIC CASINO ---\n\n")
start_list = ["START", "S"]
exit_list = ["EXIT", "E"]
add_list = ["ADD", "A"]
money_amount = int(input("Please insert money: "))
player.add_money(money_amount)
while True:
    option = input("\n\nOptions:"
                   "\n - Press -> [S]tart the game: "
                   "\n - Press -> [E]xit the game: "
                   "\n - Press -> [A]dd more money: "
                   "\nChoose: ")
    if option.upper() in start_list:
        print(player.play())
    elif option.upper() in exit_list:
        balance = player.balance
        player.remove_money(balance)
        print("\n\nThank you for playing!\n\n")
        break
    elif option.upper() in add_list:
        money_amount = int(input("\n\nPlease insert money: "))
        player.add_money(money_amount)
    else:
        print("\n\nInvalid options!"
              "\nPlease, try again!")
