print('Welcome to Rock_Paper_Scissors game')
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

#Write your code below this line 👇
import random

list=[rock,paper,scissors]



print(f'''\
please note the symbols
0 for rock :{rock}\n
1 for paper :{paper}\n
2 for scissors :{scissors}\n
''')              

just_one_game=False
willing_to_play_until_you_win=False

ask=int(input('Willing to play until you win(1) or just one game (0): '))

if ask==1:
    willing_to_play_until_you_win=True    
else:
  just_one_game=True

while willing_to_play_until_you_win:
    your_choice=int(input('Please make your choice: '))
    computer_choice=random.randint(0,2)

    
    if your_choice > 2 or your_choice < 0:
      print('What the heck you just typed,Its invalid!!')
      
    elif 1:
        print(f'your_choice is {your_choice}')
        print(list[your_choice])
        print()
        print()
        print(f'computer_choice is {computer_choice}')
        print(list[computer_choice])
        print()

        if your_choice > 2 or your_choice < 0:
          print('What the heck you just typed,Its invalid!!')

        elif computer_choice == your_choice:
            print("IT'S A TIE")

        elif computer_choice==2 and your_choice==0:
            print("YOU WIN!!!!")
            willing_to_play_until_you_win=False

        elif  computer_choice==0 and your_choice==2:
            print("YOU LOOSE!!!!")

        elif computer_choice>your_choice:
            print("YOU LOOSE!!!!") 

        else:
            print("YOU WIN!!!!")
            willing_to_play_until_you_win=False





while just_one_game:
    your_choice=int(input('Please make your choice: '))
    computer_choice=random.randint(0,2)

    if your_choice > 2 or your_choice < 0:
      print('What the heck you just typed,Its invalid!!')

    elif True:
        print(f'your_choice is {your_choice}')
        print(list[your_choice])
        print()
        print()
        print(f'computer_choice is {computer_choice}')
        print(list[computer_choice])
        print()


    if computer_choice == your_choice:
        print("IT'S A TIE")

    elif computer_choice==2 and your_choice==0:
        print("YOU WIN!!!!")
        

    elif  computer_choice==0 and your_choice==2:
        print("YOU LOOSE!!!!")

    elif computer_choice>your_choice:
        print("YOU LOOSE!!!!") 

    else:
        print("YOU WIN!!!!")
        
    just_one_game=False




