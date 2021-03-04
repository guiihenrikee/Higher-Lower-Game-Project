from art import *
from replit import clear
import random
from game_data import data
def choice():
  data_choice = random.choice(data)
  return data_choice
answer = True
a = choice()
b = choice()
print(logo)
score = 0 
while answer:  
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  if (a['follower_count']) > (b['follower_count']) and answer == "A":
    score += 1
    clear()
    print(logo)
    a = b
    b = choice()
    print("Your score is: ",score)    
  elif (b['follower_count']) > (a['follower_count']) and answer == "B":
    score += 1
    clear()
    print(logo)
    a = b
    b = choice()
    print("Your score is: ",score)  
  elif (a['follower_count']) == (b['follower_count']):
    print("Same amount if followers.")
    clear()
    a = b
    b = choice()
    print("Your score is: ",score)  
  elif (b['follower_count']) > (a['follower_count']) and answer == "A":
    clear()
    print(logo)
    print("Sorry, that's wrong. Final score: ", score)
    answer = False
  elif (a['follower_count']) > (b['follower_count']) and answer == "B":
    clear()
    print(logo)
    print("Sorry, that's wrong. Final score: ", score)
    answer = False