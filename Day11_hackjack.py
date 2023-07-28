'''       \* HackJack Capston Game *\            Date : 06-10=2022     Time- 11:40pm

Today we are going to Creat A Game having name HackJack '''

from os import terminal_size
import random

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
input1=[]
input2=[]


''' here pointer1= Mine    ANd   Pointer2= computer 
    Input1= My input    And  Input2= computer input'''

card1=random.choice(card)
input1.append(card1)
card2=random.choice(card)
input1.append(card2)
if sum(input1)==21:
    print("input1 is  won")
elif sum(input1)>21:
    print("game over")

c_card1=random.choice(card)
input2.append(c_card1)
c_card2=random.choice(card)
input2.append(c_card2)
if sum(input2)==21:
    print("you won")
elif sum(input2)>21:
    print("game over")

want=input("Whether you want to take a new card or not: ? if yes type 'yes' : ").lower()
while want=="yes":
    def continuer():
        new_card=random.choice (card)
        input1.append(new_card)
        
        input2.append(random.choice(card)) 
        
        print("input1 is :",input1)
        print("input2 is :",input2)
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
pointer2=sum(input2)
print("pointer of the input1 is :",pointer)
print("pointer of the input2 is :",pointer2)

        
# 40.if sum(input2)>21:
        #     print("game over")
        #     break
        # else:
        #     continue

# 12th line (copy paste)This code for mine ( I have to choose card here)
# let's begin with all the best wisheh
# term=input(" whose term is right now?: ")
# terms=""
# terms=term
# if term==mine:
# def starting_cond():
#     card1=random.choice(card)
#     input1.append(card1)
#     card2=random.choice(card)
#     input1.append(card2)
# starting_cond()
#38. if sum(input1)>21:
        #     print("game over")
        #     # break

        # else:
             
        #     continue





