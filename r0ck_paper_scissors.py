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
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice==0:
    print(f"You chose: \n{rock}\n")
    print(f"Computer chose: \n{rock}\n")
    print("It's a Draw!")
elif choice==1:
    print(f"You chose: \n{paper}\n")
    print(f"Computer choose: \n{paper}\n")
    print("It's a Draw!")
elif choice==2:
    print(f"You chose: \n{scissors}\n")
    print(f"Computer chose: \n{scissors}\n")
    print("It's a Draw!")
else:
    print("Enter valid choices.")
