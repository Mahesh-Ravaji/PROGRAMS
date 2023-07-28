# ''' let's build a project of code guessing No '''
# # let's begin now 
# 
# # let's begin now 
# 
# 
# 
# print(" welcome to the Number Guessing game..!!")
# print (" I am thinking of Number between 1 t0 100.")
# print(" You have 10 attempts... try to guess correct!!!")
# level=input("which level you want to choose whether hard or easy: ").lower()
# print(level)
# if level=="hard":
#     n=5
# elif level=="easy":
#     n=10
# print(f"you have {n} turns to guess let's start guessing!!! ")
# my_no=50
# #attempt=10
# 
# def guess_no():
#     while 't' !=1:
#         for j in range(0,n):
#             attempt=(10-j)
#             no=int(input(" enter the guess no.."))
# 
#             if no ==my_no:
#                 print(" You won ")
#                 't' !=0
#             
#             elif (no >=(my_no+10)):
#                 print ("too High")
#                 
#             elif (no >=(my_no+5) or no<=(my_no-5)):
#                 print ("Some what near..1")
# 
#             elif( no <=(my_no+10)):
#                 print ("too Low")
#             attempt=attempt-1
#             
#             if attempt==0:
#                 print("you lose .. , better luck next time ,try again")
# 
#             print(f"you have {attempt} attempts is remaining...!")
# 
# guess_no()
# 
#


# def str1(a):
#     #str1=input("Enter the string which you want to enter ")
#     str2=a[: :-1]
#     if str1==str2:
#         print("given string is palindrome")
#     else:
#         print("gievn string is not palindrome")
# str1("mahesh")
# 
# #code for picke index for picke an array
# import array
# 
# Print ("welcome to the tick tak toe game .. !!! ")
# 
# print("choose whether you want to choose hard level or Easy level..!!")
# arr tak_toe(3,3)=[]
#


list1=['A','B','C','D','X'] #CRICKET
list2=['E','F','A','C','Y'] #BADMINTON
list3=['B','D','E','F','Z'] #FOOTBALL
r1=[]
r2=[]
a=[]
r3=[]
b=[]
r4=[]
# def func1():
#     for i in list1:
#         for j in list2:
#             if(i==j):
#                 r1.append(i)
#             print("List ofstudents who play both cricket and badminton:",r1)
# func1()

def func2():
    for i in list1:
        f=0
        for j in list2:
            if(i==j):
                f=f+1
            if(f==0):
                r2.append(i)
#                     print("List ofstudents who play either cricket or badminton but not both:",r2)
        for j in list2:
            f=0
            for i in list1:
                if(i==j):
                    f=f+1
                if(f==0):
                    r2.append(j)
                    print("List ofstudents who play either cricket or badminton but not both:",r2)
func2()
# def func3():
# for i in list1:
# for k in list3:
# if(i==k):
# a.append(i)
# for j in list2:
# for k in list3:
# if(j==k):
# a.append(j)
# for k in list3:
# f=0
# for l in a:
# if(k==l):
# f=f+1
# if(f==0):
# r3.extend(k)
# print("List of students who neither play cricket nor badminton:",r3)
# print("Number ofstudents who neither play cricket nor badminton:",len(r3))
# func3()
# def func4():
# for i in list1:
# for k in list3:
# if(i==k):
# b.append(i)
# for l in b:
# f=0
# for j in list2:
# if(l==j):
# f=f+1
# if(f==0):
# r4.append(l)
# print("List of students who play cricket and football but not badminton:",r4)
# print("Number ofstudents who play cricket and football but not badminton:",len(r4))
# func4()
# 
# 
# 
# 
# 
#
print ("helo world '")
