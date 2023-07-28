# DAY 4                                                            DATE 30-5-22
#  IN THIS SESSION WE ARE GOING TO LEARN 🙂RANDOMIZATION😎😲

# import random
# random_integer=random.randint(1,10) # it starts from 1 and in between 10 not equal to 10
# print(random_integer)

# #0.0000000 - 0.999999999
# random_float=random.random()    # it starts from 0 to 1 indirectly 
# print(random_float)

# # random_float=random.randfloat(0.0,0.5)
# # print(random_integer)

# randomfloat=random.random() *5
# print(randomfloat)

# love_score= random.randint(1,100)
# print(f"Your love score is {love_score}")

# # DAY 4.1 EXERCISE
# # HEAD OR TAILS ( Coding Exercise)                                                          #31-5-22
# random_side=random.randint(0,1)
# # here 0 is head and 1 is tail
# if random_side == 0:
#     print("tails")
# else:
#     print("tails")


# # DAY 4.3 (DATA STRUCTURE - LIST)

# brothers=["suresh","akash","mahesh"]
# brothers[1]="aakash"    # we can 🙂change🙃 perticular value of list by spacifing than value
# print(brothers)

# brothers.extend(["sunil","anil"])
# print(brothers)
# # b2=['atharv','dhamyaa']  # some erros is occured try next time
# # brothers.insert([b2])
# print(brothers)


# use of SPLIT function                                  # SPLIT - (" , ")
# '''split function add anything in the form of list by specified quotation '''

# names_string=input("give me everybody's names, sepersated by a comma. ")
# names=names_string.split(",")
# print(names)
# print(names[0])
# # get the total no of items
# print(len(names))
# num_items=len(names)

# import random
# random_choice=random.randint(0, num_items-1)
# print(random_choice)
# person_who_will_going_to_pay_today=names[random_choice]
# print("person is going to pay is " + person_who_will_going_to_pay_today )

# random.choice() funtion is used to generate/accese  a random vlaue from a lsit 
# print(random.choice(names))

# we can add list into the list o
'''New thing we learned here,😎😊😉'''
fruits=["apple", "banana", "mango","pears","grapes","pineapple"]
vegetables=["tomato","onion","potatos","kali","pinache"]
# dirty_dozons=[fruits ,vegetables]
# print(dirty_dozons)
# print("final answer= ",dirty_dozons[1] [3])

# CHESS LOCATION PROBLEM
'''LIST used as matrix'''
row1=[" ", "👨🏼 ", " "]
# row2=[" ", " ", " "]
# row3=[" ", " ", " "]
# matrix=([row1, row2, row3])
# print(matrix)

# p=(f"{row1}\n{row2}\n{row3}\n")

# position=input("where do you want to put the treasure" )
# vertical=int(position[0])
# horizontal=int(position[1])
# # print(matrix[vertical-1])
# # print(matrix[horizontal-1])
# matrix[vertical -1] [horizontal-2]="K"
# matrux[horizontal - 1] = "K"
# selecte_row=matrux[horizontal - 1]="K"
# selecte_row=matrux[horizontal - 1]
# print(f"{row1}\n{row2}\n{row3}")



''' TRY THIS CODE AND SOLVE AGIAN AND AGIAN UNTIL YOU CAN UNDERSTAND THE CODE HOW IT IS WORKS 
AND TRY TO IMPORVE YOUR DEBUGGING SKILLS '''
import random
rock=0
paper=1
sizor=2

# game=[rock, paper, sizor]                 #


u=int(input("enter no 0 for rock, 1 for paper, 2 for sizor : "))

# if game[u]>=3 or game[u]<=0 :
#     print("plz enter valid number")
# else:
c=random.randint(0,2)
print("computer choice " ,c)
print("user choice",u)
    # print( game[u>=3 or u<=0]=="enter valid number")                              #
if c==0 and u==2 :
    print("you lose😮")
elif c==0 and u==1 :
    print("you lose😌!!")
   
elif c==1 and u==2 :
    print("you win!")
elif c==0 and u==0 :
    print ("mathch drawn , keep trying!")
elif c==2 and u==2 :
    print("mathch drawn , keep trying!!")

elif (c==1 and u==1 )  :
    print ("match is drawn, keep trying !!! ")
else:
    print("enter valid number")
                                                                                         # END 4TH DAY 4-6-22
   