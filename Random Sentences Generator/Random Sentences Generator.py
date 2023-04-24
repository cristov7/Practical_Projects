import random


def get_random_word(words_list: list):
    word = random.choice(words_list)
    return word


print("""
                       WELCOME TO MY:
                "RANDOM SENTENCES GENERATOR"  

""")


first_names_list = ["Cristiano", "Lionel", "Robert"]
last_names_list = ["Ronaldo", "Messi", "Lewandowski"]

born_dates_list = ["05.February.1985", "24.June.1987", "21.August.1988"]
born_places_list = ["Madeira, Portugal", "Rosario, Argentina", "Warsaw, Poland"]

football_leagues_list = ["Premier League", "La Liga", "Bundesliga"]
club_teams_list = ["Manchester United", "Barcelona", "Bayern Munich"]
national_teams_list = ["Portugal", "Argentina", "Poland"]

player_positions_list = ["winger", "forward", "striker"]
player_numbers_list = [7, 10, 9]


first_name = get_random_word(first_names_list)
last_name = get_random_word(last_names_list)

born_date = get_random_word(born_dates_list)
born_place = get_random_word(born_places_list)

football_league = get_random_word(football_leagues_list)
club_team = get_random_word(club_teams_list)
national_team = get_random_word(national_teams_list)

player_position = get_random_word(player_positions_list)
player_number = get_random_word(player_numbers_list)


print(f"This is {first_name} {last_name}."
      f"\nHe was born on {born_date} in {born_place}."
      f"\n{last_name} is a captain both {football_league} club {club_team} and the {national_team} national team."
      f"\nDefinitely the greatest {player_position} ever who plays with number {player_number}!")


print("""

              THANK YOU FOR USING MY GENERATOR!
""")
