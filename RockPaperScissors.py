import random


# Function to determine the winner
def determine_winner(player, computer):
    a = (player == "rock" and computer == "scissors")
    b = (player == "scissors" and computer == "paper")
    c = (player == "paper" and computer == "rock")
    winning_combinations = a or b or c

    if player == computer:
        return "It's a tie!"
    elif a or b or c:
        return "player"
    else:
        return "computer"


# Main game function
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0

    while True:
        print("\nRock, Paper, Scissors - let's play!")
        player_choice = input("Enter either rock, paper, scissors, or exit to quit the game: ")

        if player_choice == 'exit':
            print("*" * 50)
            print(f"You won {player_wins} times.")
            print(f"The computer won {computer_wins} times.")
            print("Thanks for playing!")
            print("*" * 50)
            break

        elif player_choice not in options:
            print("Invalid choice! Choose either rock, paper, or scissors (or exit)!")
            print("*" * 50)
            continue

        computer_choice = random.choice(options)
        print("*" * 50)
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print("*" * 50)

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            print("You win!")
            player_wins += 1
        elif result == "computer":
            print("You lose!")
            computer_wins += 1


rock_paper_scissors()
