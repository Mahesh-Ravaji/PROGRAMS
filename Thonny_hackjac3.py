import random 
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
P1=[]
P2=[]

# print(sum(card))
# sum(P1)<21==True
# while True:
#     card1=random.choice(card)
#     P1.append(card1)
#     card2=random.choice(card)
#     P1.append(card2)
#     print(P1)
# 
#     # First Conditions for Hackjack capston game
#     if sum(P1)==21:
#         print("input1 is  won")
#     elif sum(P1)>21:
#         print(P1)
#         print("game over")
#         sum(P1)<21==False
#         
# #         sum(P1)<21==False
#         break
#     
#     else:
#         new_card=input("whether you want to take new card or not:? if yes type yes: ").lower()
#         if new_card=="yes":
#             def should_continue():
#             
#            
#                 if new_card=="yes": 
#                     n_card3=random.choice(card)
#                     P1.append(n_card3)
#                     print(P1)
#                 elif new_card=="no":
#                     print("See you agian:")
#             
#             
# #             new_card=input("whether you want to take new card or not:? if yes type yes: ").lower()
# #             if new_card=="yes":
# #                 card4=random.choice(card)
# #                 P1.append(card4)
# #                 print(p1)
#             if sum(P1)<21==True:
#                 should_continue()
#             else:
#                 print("game over")
#                 sum(P1)<21==False
#

# sum(P1)==True
sum_p1="True"

if sum(P1)==21:
    print(f"{P1} is won")
elif sum(P2)==21:
    print(f"{P2} is won")
    
def should_continue():
    cards.append(random.choice(P1))

while sum(P1)==True:
    if sum(P1)<21:
        cards=input("whether you want to take a new card or not if yes then type yes")
        if cards=="yes":
            should_continue()
            
    