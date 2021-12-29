import random
user_name = input("Enter your name:")
user_choice = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["Rock", "Paper", "Scissors"]
jarvis_choice = random.choice(possible_actions)
print(f"\n {user_name} chose {user_choice}, Computer chose {jarvis_choice} \n")

if user_choice == jarvis_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "Rock":
    if jarvis_choice == "Scissors":
        print("Rock smashes Scissors! You Win!")
    else:
        print("Paper covers Rock! You Lose.")
elif user_choice == "Paper":
    if jarvis_choice == "Rock":
        print("Paper covers Rock! You Win!")
    else:
        print("Scissors cuts Paper! You Lose.")
elif user_choice == "Scissors":
    if jarvis_choice == "Paper":
        print("Scissors cuts Paper! You Win!")
    else:
        print("Rock smashes Scissors! You Lose.")

exit (0)