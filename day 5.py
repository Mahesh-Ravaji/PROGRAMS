'''IN the day 5th we are going to learn abot                             # 4th june 2022
      FOR LOOPS , RANGE AND CODE BLOCKS
      HERE WE GENERATED A 😎🙃PASSWORD🤪 THAT SEE AGIAN AND TRY TO UNDERSTAND CLEARLY '''

# fruits= ["apple", "orange", "pear"]
# for fruit in fruits :
    # print(fruit)                 # run this you understand aout of for loop works
    # print(fruit + " sweet ")  

# print(fruits)                     # this will execute after for loop end hence indentaion is very important


# a=[3]
# s=4
# a.append(s)
# print(a)

# # program to calculate AVERAGE HEIGHT 
# students_height=int(input("input a list of students height : \n").split())
# average=[ ]
# print(average.append[students_height])
# # print(sum(ag))

# length=(len(students_height ))
# average_of_students_height=sum(ag)/length
# print(average_of_students_height)


# student_heights=input("input a list of strudent heights ").split()
# for n in range(0,len(student_heights)):
#     print(student_heights[n])
# #     student_heights[n]=student_heights[n]
# # print(student_heights)
#     print(n)



# ''' write a progrma to py password gernatrator  😎😏 '''
# import random
# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
#         'p','q','r','s','t','u','v','w','x','y','z',]
# numbers=['1','2','3','4','5','6','7','8','9',]
# symbols=['!','<','>','@','#','$','%','&','*','(',')','+','/']

# print("welcome to py password gernarator ")
# nr_letters=int(input("how many letter password you have to genrator ...?\n"))
# nr_numbers=int(input("how many numbers password you have to genrator ...?\n"))
# nr_symols=int(input("how many symblos password you have to genrator ...?"))
 
# for char in range (1,nr_letters +1) :
#     random_char=random.choice(letters)
#     print(random_char,end='')

# for num in range (1,nr_numbers +1):
#     random_num=random.choice(numbers)
#     print(random_num,end='')

# for symbol in range (1,nr_symols+1):
#     random_symbol=random.choice(symbols)
#     print(random_symbol,end='')

# print("    your passoword is here..!!")
# print(random_char+random_num+random_symbol,'\n')
    # print(random.choice(letters)+random.choice(numbers)+random.choice(symbols))

''' SHUFFLE the list using shuffle function '''
import random 
list1=[1,2,3,4,5,6,7,8,9]
random.shuffle(list1)
print(list1)

'''  how to use append function in different way or by using operator (+=) '''
password=''
for char in password:
    password+=char
