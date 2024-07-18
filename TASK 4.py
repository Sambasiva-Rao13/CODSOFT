import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice! Enter again (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()