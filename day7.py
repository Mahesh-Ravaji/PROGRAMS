word_list=["ardvark","baboon","camel"]
import random
choosen_word=random.choice(word_list)
guess=input("guess an character")
character=guess.lower()

for store in word_list:
    if guess==choosen_word:
        print("true")
    else:
        print("false")