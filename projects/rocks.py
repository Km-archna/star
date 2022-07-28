import random
print("Hii, my name is Archana")

def play():

    possible_term = ["rock", "paper", "scissors"]
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(possible_term)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


if __name__ == "_main_":
   while True:
      play()
      choce = input(" do you want to roll the dice again (y/n) ")
      if choce.lower() == 'n':
         break