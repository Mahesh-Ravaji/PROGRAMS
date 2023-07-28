'''       \* HackJack Capston Game *\            Date : 06-10=2022     Time- 11:40pm

Today we are going to Creat A Game having name HackJack '''

import random

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
input1=[]
input2=[]

# This code for mine ( I have to choose card here)
# let's begin with all he best wisheh
# def starting_cond():
#     card1=random.choice(card)
#     input1.append(card1)
#     card2=random.choice(card)
#     input1.append(card2)
# starting_cond()

want=input("Whether you want to take a new card or not: ? if yes type 'yes' : ").lower()
while want=="yes":
    def continuer():
        new_card=random.choice (card)
        input1.append(new_card)
        print(input1)
        print(card)
        
    continuer()   # function called
    want2=input("Whether you want to take a new card or not: ? if yes type 'yes' : ").lower()
    if want2=="yes":
        want="yes"
        continue
    else:

        want="no"

    #pass

# step 3 TODO:
pointer=sum(input1)
print(pointer)

        








