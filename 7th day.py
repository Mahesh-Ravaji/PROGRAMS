

import random
word_list=["mahesh","suresh","akash"]
chosen_word=random.choice(word_list)
print(f'psst, the solutin is {chosen_word}.')

guess=input("guess a letter:").lower()

for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("wrong")