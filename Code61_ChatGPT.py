import random

def rock_paper_scissors():
    options = ["Rock", "Paper", "Scissors"]
    player_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    
    if player_choice not in options:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    computer_choice = random.choice(options)
    print(f"The computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
rock_paper_scissors()