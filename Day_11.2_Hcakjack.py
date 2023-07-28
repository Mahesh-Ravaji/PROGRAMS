import random 
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
P1=[]
P2=[]

print(sum(card))
sum(P1)<21==True

card1=random.choice(card)
P1.append(card1)
card2=random.choice(card)
P1.append(card2)
print(P1)
while True:

    # First Conditions for Hackjack capston game
    if sum(P1)==21:
        print("input1 is  won")
    elif sum(P1)>21:
        print(P1)
        print("game over")
        sum(P1)<21==False
        
#         sum(P1)<21==False
        break
    
    else:
        new_card=input("whether you want to take new card or not:? if yes type yes: ").lower()
        def should_continue():
            
           
            if new_card=="yes":
                n_card3=random.choice(card)
                P1.append(n_card3)
                print(P1) 
            elif new_card=="no":
                print("See you agian:")
            
            
#             new_card=input("whether you want to take new card or not:? if yes type yes: ").lower()
#             if new_card=="yes":
#                 card4=random.choice(card)
#                 P1.append(card4)
#                 print(p1)
            if sum(P1)<21==True:
                should_continue()
            else:
                print("game over")
                sum(P1)<21==False
                    






import random

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10]

str=int(input("type 1 if you want to continue or else 0"))
# let's play the lower higher level game of stockmarket...
print ("what you think is stock market prize will get higher or lower ..?")
if str==1
