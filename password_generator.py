
import random
import string
import os
from datetime import datetime


#load words from file
def load_words():
    words = []
    try:
        with open("top_english_nouns_lower_100000.txt", "r") as file:
            for line in file:
                words.append(line.strip())
    except FileNotFoundError:
        print("Word file not found.")
    return words


#generate memorable password
def memorable_password(num_words=3, case="lower"):
    words = load_words()
    chosen = []

    for i in range(num_words):
        word = random.choice(words)
        number = str(random.randint(0, 9))

        if case == "upper":
            word = word.upper()
        elif case == "title":
            word = word.capitalize()

        chosen.append(word + number)

    password = "-".join(chosen)
    save_password(password, "Memorable")
    return password


# generate random password
def random_password(length=10, use_punctuation=True, banned_chars=""):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if use_punctuation:
        chars += string.punctuation

    for c in banned_chars:
        chars = chars.replace(c, "")

    password = ""
    for i in range(length):
        password += random.choice(chars)

    save_password(password, "Random")
    return password


# save password to file
def save_password(password, folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

    path = os.path.join(folder, "Generated_Passwords.txt")
    time_now = datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")

    with open(path, "a") as file:
        file.write(password + " | Created at: " + time_now + "\n")


# test generator
def test_generator():
    for i in range(1000):
        if random.choice([True, False]):
            memorable_password()
        else:
            random_password()


# main program
if __name__ == "__main__":
    print("Password Generator")

    choice = input("Choose password type (memorable/random): ").lower()

    if choice == "memorable":
        words = int(input("How many words? "))
        case = input("Case (lower, upper, title): ")
        print("Password:", memorable_password(words, case))

    elif choice == "random":
        length = int(input("Password length: "))
        punct = input("Include punctuation? (yes/no): ").lower() == "yes"
        banned = input("Characters not allowed: ")
        print("Password:", random_password(length, punct, banned))

    else:
        print("Invalid choice")

    test_generator()
