#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Rock
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#print(Rock)
#print(Paper)
#print(Scissors)


import random
game_image=[Rock, Paper, Scissors]

user=int(input("What do you choose ? type 0 for Rock,  1 for Paper OR 2 for Scissors. \n "))
print(f'You Chose {user}')
if user >3 or user <0:
    print('You have entered invalid number, Game over!!!')
else :
    print(game_image[user])
    
    computer=random.randint(0,2)
    
    #print(f"You chose  {user}")
    print(f"Computer chose {computer}")
    print(game_image[computer])


    if user == 0  and computer == 2:
           print(' You Win (smile)')
        
    elif computer ==0 and user == 2:
        
        print('You lose')
        
    elif computer > user :
        print('You lose')
        
    elif user > computer :
        print('You win')
        
    else :
        
        
        print(" Its a draw ")
    


# In[ ]:




