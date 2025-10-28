# EXERCISE 5
# Sanke Water Gun Game
# 1.Snake Water and Gun is a variation of the chilfern's game "rock-paper-scissors" where player use hand gesture to represent a snake, water or gun. The gun beats the snake, the water bests the gun, and the snake beats the water.
# 2.Write a python program to create a sanke water gun game in python using if-else statemnets. Do not create any fancy GUI. Use proper functions to check for win.

# 3.Sample Input and Output
#                   S W G                            
#   Computer =      0 1 2
#   Player =    S 0 D W L
#               W 1 L D W
#               G 2 W L D



import random

def check_win(user, computer):
    """
    Determines the winner between user and computer.
    Rules:
    - Snake drinks water → Snake wins
    - Water douses gun → Water wins
    - Gun shoots snake → Gun wins
    """
    if user == computer:
        return "Draw"

    if (user == 'snake' and computer == 'water') or \
       (user == 'water' and computer == 'gun') or \
       (user == 'gun' and computer == 'snake'):
        return "You Win"
    else:
        return "Computer Wins"

def main():
    print("=== Snake Water Gun Game ===")
    options = ['snake', 'water', 'gun']
    
    user_choice = input("Enter your choice (snake/water/gun): ").strip().lower()
    
    if user_choice not in options:
        print("Invalid choice! Please choose snake, water, or gun.")
        return

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = check_win(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
