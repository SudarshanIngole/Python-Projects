#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1.lower() + name2.lower()
true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
  
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}., you can be partners")


# In[ ]:




