''' let's build a project of code guessing No '''
# let's begin now 

print(" welcome to the Number Guessing game..!!")
print (" I am thinking of Number between 1 t0 100.")
print(" You have 10 attempts... try to guess correct!!!")

my_no=14
#attempt=10
def guess_no():
    for j in range(1,11):
        attempt=10

        guess_no=int(input(" enter the guess no.."))

        global new_attempt #=attempt-1
        new_attempt=attempt-1
        if guess_no ==my_no:
            print(" You won ")
        
        elif guess_no <guess_no-10:
            print ("too High")

        elif guess_no <guess_no-10:
            print ("too two")
            
        print(f"you have {new_attempt} attempts is remaining...!")

guess_no()



