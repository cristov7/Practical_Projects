import random
print("""
                       WELCOME TO MY:
                "RANDOM SENTENCES GENERATOR"

""")


def get_random_word(words: list):
    return random.choice(words)


names_list = ["Peter", "Michell", "Jane", "Steve"]
places_list = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs_list = ["eats", "holds", "sees", "plays with", "brings"]
nouns_list = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs_list = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details_list = ["near the river", "at home", "in the park"]
print("Hello this is you first random sentence:")
while True:
    random_name = get_random_word(names_list)
    random_place = get_random_word(places_list)
    random_verb = get_random_word(verbs_list)
    random_noun = get_random_word(nouns_list)
    random_adverb = get_random_word(adverbs_list)
    random_detail = get_random_word(details_list)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.\n\n")
    command = input("Click [Enter] to generate new one.")
    if command == "":
        continue
    else:
        print("""

              THANK YOU FOR USING MY GENERATOR!
        """)
        break
