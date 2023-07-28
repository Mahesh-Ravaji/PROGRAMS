''' write a python program to make a new calculator '''

# step 1: create a function of each operations 

#Add
def add(n1,n2):
    return (f"additon of {n1} and {n2} is equal to {n1+n2} " )
#Substract
def subtract(n1,n2):
    return (f"subtraction of {n1} and {n2} is equal to {n1-n2} " )

# mulitply 
def multiply (n1,n2):
    return (f"Multiplication of {n1} and {n2} is equal to {n1*n2} " )

# division
def divide (n1,n2):
    return (f"Division of {n1} and {n2} is equal to {n1/n2} " )

# Make a New Ditionary of Operations
# x=int(input("enter the fisrt value: "))
operations= {"+":add,
 "-":subtract, 
 "/":divide, 
 "*":multiply
  }
print(f"{operations.keys()}")
should_continue=True
def calculator():
    while (should_continue ) :

        oop=input("Which operation you have to perform from the above : ?")
        x=int(input("enter the fisrt value: "))
        y=int(input("enter the 2nd value: "))
        perform=operations[oop]
        past_ans=perform(x,y)
        print(past_ans)
        if (input("you have to continue if yes then type 'y' or start new then type 'n'"))==y:
            x=past_ans
        else:
            should_continue=False
            calculator()
calculator()

    # ask to user to whether he have to performs an actions on previous output or 
    # peroom  on next action

    # another_operation=input("chose the other operation which you have to perfom")
    # z=int(input("Enter the 3rd number : "))

    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    # perform=operations[another_operation]
    # new_ans=perform(past_ans,z)

    # seconde_ans=(f"{past_ans} {another_operation} {z} = {new_ans}")
    # print(seconde_ans)

    
