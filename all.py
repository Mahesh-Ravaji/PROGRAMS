# # from replit import clear                                                    #scroll Down for your code
# # from art import logo
# # print(logo)
# 
# bids = {}
# bidding_finished = False
# 
# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
# 
# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no':")
# 
#   if should_continue == "no":
# 
#     bidding_finished = True
#     find_highest_bidder(bids)
#   else:
#     continue
# #   elif should_continue == "yes":
#     # clear()
#   
# 
# # '''
# # FAQ: My console doesn't clear()
# 
# # This will happen if you're using an IDE other than replit. 
# # I'll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 
# 
# # https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076'''
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # people=int(input("Enter the no of peoples are bedding:? "))
# # dict_arey={}
# # for i in range (0,people):
# #     new_dict={}
# #     # opinion='type s if people of bedder are remaining and vice versa'
# #     def bed(name,bid ,opinion):
# #         
# #         new_dict["name"]=name
# #         new_dict["bid"]=bid
# #         new_dict["opinion"]=opinion
# # 
# #     n=input("Enter Your name..? ")
# #     b=int(input("Enter your bid.? "))
# #     op=input("Enter yes if bed wansts to continue..else enter no?")
# #     bed(n,b,op)
# # #     dict_arey.append(new_dict)
# #     if op=="yes":
# #         continue
# #     else:
# #         break
# #     print(new_dict)
# #     # dict+=(new_dict)
# # print(dict_arey)
# 
# 
# '''       \* HackJack Capston Game *\            Date : 06-10=2022     Time- 11:40pm
# 
# Today we are going to Creat A Game having name HackJack '''
# 
# from os import terminal_size
# import random
# 
# card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# input1=[]
# input2=[]
# 
# 
# 
# ''' here pointer1= Mine    ANd   Pointer2= computer 
#     Input1= My input    And  Input2= computer input'''
# card1=random.choice(card)
# input1.append(card1)
# card2=random.choice(card)
# input1.append(card2)
# if sum(input1)==21:
#     print("input1 is  won")
# elif sum(input1)>21:
#     print("game over")
# c_card1=random.choice(card)
# input2.append(c_card1)
# c_card2=random.choice(card)
# input2.append(c_card2)
# if sum(input2)==21:
#     print("you won")
# elif sum(input2)>21:
#     print("game over")
# 
# want=input("Whether you want to take a new card or not: ? if yes type 'yes' : ").lower()
# while want=="yes":
#     def continuer():
#         new_card=random.choice (card)
#         input1.append(new_card)
#         if sum(input1)>21:
#             print("game over")
#             # break
# 
#         else:
#              
# #               continue
#         input2.append(random.choice(card))
#         if sum(input2)>21:
#             print("game over")
#             break
#         else:
#             continue
#         print("input1 is :",input1)
#         print("input2 is :",input2)
#         print(card)
#         
#     continuer()   # function called
#     want2=input("Whether you want to take a new card or not: ? if yes type 'yes' : ").lower()
#     if want2=="yes":
#         want="yes"
#         continue
#     else:
# 
#         want="no"
# 
#     #pass
# 
# # step 3 TODO:
# pointer=sum(input1)
# pointer2=sum(input2)
# print("pointer of the input1 is :",pointer)
# print("pointer of the input2 is :",pointer2)
# 
#         


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

import random 
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
P1=[]
P2=[]

print(sum(card))
sum(P1)<21==True
while True:
    card1=random.choice(card)
    P1.append(card1)
    card2=random.choice(card)
    P1.append(card2)
    print(P1)

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
        def should_continue():
            
            new_card=input("whether you want to take new card or not:? if yes type yes: ").lower()
            if new_card=="yes":
                n_card3=random.choice(card)
                P1.append(n_card3)
                print(P1)
            else:
                should_continue()
            
            
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
                    
            




















