# # create a blank
# dispaly=[]
# for i in range (word_length):
#     display+="_"
#     
# '''# TODO-1:- Use a whiel loop to let the user guess again. The loop should only
# stop once the user has guessed all the letters in the chosen_word and "display"
# no moer blank("_") . then you can tell the user they've won.'''
# 
# end_of_game= false
# while not end_of_game :
#     guess = input("Guess the letter:" ).lower()
#     
#     # check guessed letter
#     for position in range (word_length):
#         letter = chosen_word[position]
#         # print(f"Current postion:{position}\n current letter :{letter}\n Guessed letter :{guess}")
#         if letter==guess:
#             display[position]=letter
#     print(display)
#     
#     # Check if there are no more "_" left in 'display' Then all letteras have been guessed.
#     if "_" not in display:
#         end_of_game= True
#         print ("You win. ")


''' we arrrrrrreee going to start '''

# here we are going to code for hangman 
''' let's try our best for this code let's begin '''

# step 1 : generatte a random word 
word=["mahesh", "suresh", "akash","Ravaji"]
blanck=[]
import random

# step 2: generate as many blanks as letter in word
random_word=random.choice(word)
for i in random_word:
    blanck+="_"
    print(blanck)

# ask the user to guess a letter 
guess_letter=random.choice(random_word)

# Is the guessd letter inn the word 
# if yes replace the blank with the letter
for j in random_word:
    if j==guess_letter:

        blanck+=j
        print(blanck)
    else:
        print("lose life")











