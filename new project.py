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
user_Choice= int(input("What do you want to choose ? Type 0 for Rock , Type 1 for paper or Type 2 for scissors? "))
if user_Choice==0:
    print(rock)
elif user_Choice==1:
    print(paper)
elif user_Choice==2:
    print(scissors)
else:
    print("Invalid entry")

computer_Choice= random.randint(0,2)
if computer_Choice==0:
    print("Computer chose: ")
    print(rock)
elif computer_Choice==1:
    print("Computer chose: ")
    print(paper)
elif computer_Choice==2:
    print("Computer chose: ")
    print(scissors)


if (computer_Choice==0 and user_Choice==1 or computer_Choice==1 and user_Choice==2 or computer_Choice==2 and user_Choice==0):
    print("You won")
elif(computer_Choice==0 and user_Choice==0 or computer_Choice==1 and user_Choice==1 or computer_Choice==2 and user_Choice==2):
    print("Draw")
else:
    print("Computer won")