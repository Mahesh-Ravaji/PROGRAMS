# class car:
#     def __init__(self, name ,cost ):
#         
#         self.name=name
#         self.cost=cost
#         
#     def car_info(self):
#         print("car name = :",self.name)
#         print("cost of the car = :",self.cost)
#         
# car_name=input("enter the car name which you want :")
# cost_of_car=int(input("Enter the cost of the car :"))
# 
# obj1=car(car_name,cost_of_car)
# obj1.car_info()
# 
# obj2=car("BMW",800000)
# obj2.car_info()

# Program to find given no is prime or not

# def prime_cheker(num):
#     
#     if num>1:
#         for i in range (2,num):
#             if num%i==0 :
#                 print(f"{num} is not prime number")
#                 breake
#         else:
#             print(f"{num} is prime number")
#                 
#     else:
#         print(f"{num} is not prime number")
# 
# prime_cheker(5)


# print("rainbow has%d color %d=7")

# write a table using formatting operator

# def tabel(num):
#     for i in range(1,11):
#         print("==========")
#         for j in range (1,11):
#             print(

    
# str=input("enter the stirn=")
# ch=input("enter the character to be searched :")
# letter=ch[0]
# for index in range (0, len(str)):
#     if(str[index]==letter):
# #          print("character",letter,"is present at",index,"index")
#          print(f"character {letter} is present at index {index}")
# 
#          break
# else:
#     print("character",letter,"is not present in given strring")
#     
        
# str=input("enter the stirn=")
# ch=input("enter the character to be searched :")
# letter=ch[0]
# for index in range(0,len(str)):
#     if str[index]==letter :
#         print(letter, index)
#     else:
#         ("character is not present")

# write a program to perform the following conditions
'''Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird '''

# let's start our code with smile                  Date : 03/09/2022

num=int(input("enter the first value : "))

for n in range (1,num):
    if n%2==0:
        print("not weird")
    elif (n%3==0):
        print("weird")
    else:
        print(num)

        for num in range (1,6):
            if num%2==0:
                print("not weird")
            else:
                print(num)

        for num in range (6,20):
            if n%2==0:
                print("weird")
            else :
                print(num)
    
    
    
print("lets do code for printing a number ")
word_list=["mahesh", "suresh", "akash"]
 
    
    
    
    
    
    










