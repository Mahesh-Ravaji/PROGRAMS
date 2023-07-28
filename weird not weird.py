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