import random

name = input("Enter your name: ")
choices = ["rock🪨", "paper📃", "scissors✂️"]

user_score = 0
computer_score = 0

while True:
    print("\n==============================")
    print("     ROCK PAPER SCISSORS   ")
    print("==============================")
    print("1. Rock🪨   2. Paper📃   3. Scissors✂️")

    user_input = input("Enter number: ")

    if user_input not in ["1", "2", "3"]:
        print("Invalid choice🚫")
        continue

    user = choices[int(user_input) - 1]
    computer = random.choice(choices)

    print("\n---------- RESULT ----------")
    print(name, "🌸:", user)
    print("Computer💻:", computer)

    if user == computer:
        print("Outcome:", "It's a tie‼️")
    elif (user == "rock🪨" and computer == "scissors✂️") or \
         (user == "scissors✂️" and computer == "paper📃") or \
         (user == "paper📃" and computer == "rock🪨"):
        print("Outcome:", name, "wins🌠")
        user_score += 1
    else:
        print("Outcome:", name, "loses💢")
        computer_score += 1

    print("----------------------------")
    print("Score → ", name, "🌸:", user_score, "\n\t Computer💻:", computer_score)
    print("==============================")

    play_again = input("Play again❓(y/n): ")
    if play_again.lower() != "y":
        break

print("\n🌼 Final Score →", name, "🌸:", user_score, "\n\t\t Computer💻:", computer_score)
print("◄◄◄◄◄◄ Thanks for playing", name, "🍂 ►►►►►")
