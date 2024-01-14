# The Snake water Gun Game in python

import random
import os
import time

print('Game Snake Water Gun Game in python')

print('Welcome The game Snake water gun game in python')
print('Before Starting the game understand the rules of the python')
print('\n Rules:--------\n 1. The Computer Will choose first. \n2. Then you have to enter your choice.\n3. The Result will displayed after choosing the write option.')

print('\n----Lets Play----')

print('You have to coose from this option 1. Snake\n2. Water\n 3. Gun')

# time.sleep(2000)

print("Computer Choice:")

print("1. Snake 2. Water 3. Gun")

list1=['Snake','Water','Gun']

def play_game():
          
          computer=random.choice(list1)
          print(f"computer Choice {computer}\n")
          
          # User Giving the three chances to choose the option
          choice=0

                    # Gving the two chances to choose the option
          while(choice<2):
                    user=input("Enter your Choice: \n")
                    
                    if user in list1:
                                        # print("Correct")

                                        if(computer=='Snake' and user=='Snake'):
                                                  print("Game Draw")
                                                  exit(0)
                                        elif(computer=='Snake' and user=='water'):
                                                  print("You loss....Snake beats water")
                                                  exit(0)
                                        elif(computer=='Snake' and user=='Gun'):
                                                  print("You Win....Gun beats Snake")
                                                  exit(0)

                                        elif(computer=='Water' and user=='Water'):
                                                  print("Game Draw")
                                                  exit(0)
                                        elif(computer=='Water' and user=='Snake'):
                                                  print("Computer Win...!!")
                                                  exit(0)
                                        elif(computer=='Water' and user=='Gun'):
                                                  print("Computer Win...!!")
                                                  exit(0)
                                        
                                        elif(computer=='Gun' and user=='Gun'):
                                                  print("Game Draw")
                                                  exit(0)
                                        elif(computer=='Gun' and user=='Snake'):
                                                  print("Computer Win...!! Gun wins against Snake.")
                                                  exit(0)
                                        elif(computer=='Gun' and user=='Water'):
                                                  print("Computer Win...!! Gun wins against Water")
                                                  exit(0)
                              
                    else:
                              print("You Entered wrong input...! Please Enter the correct input again")
                              print("Enter Corrct Input")
                              choice+=1

play_game()
