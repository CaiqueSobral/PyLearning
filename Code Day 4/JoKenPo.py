import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

player_choice = int(input("Digite 0, 1 ou 2, onde: 0=Pedra, 1=Papel, 2=Tesoura. "))
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose")
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose.")
    elif computer_choice > player_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win")
    elif computer_choice == player_choice:
        print("It's a draw")