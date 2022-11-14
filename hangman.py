import random
import hangman_words
import hangman_art
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
display = []

for letter in chosen_word:
  display.append("_")

wrong_list = []
trial = 0
while "_" in display and trial < 7:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in list(chosen_word):
    trial += 0 
    if guess in display:
      print(f"You have already tried '{guess}'.")
  else:
    if guess in wrong_list:
      trial += 0
      print(f"You have already tried '{guess}'.")
    else:
      wrong_list.append(guess)
      print(hangman_art.lives[trial])
      trial += 1
  position = -1
  for letter in chosen_word:
    position += 1
    if letter == guess:
      display[position] = letter
  result_string = " ".join(display)
  print(result_string)
  print("\n")
  
if not "_" in display:
  print("You Win!!!!!!!!")
else:
  print(f"You Lose!!!\nThe correct answer was '{chosen_word}'.")
