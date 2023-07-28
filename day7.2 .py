# write a program to pick a random number and check a ans
# import random
# word_list=["mahesh", "suresh", "akash"]
# guess_word=random.choice(word_list)

# guess_letter=random.choice(guess_word)
# print(guess_letter)
# 
# for j in guess_word:
#     if j==guess_letter :
#         print("right ")
#         break
# #     else:
#         print("wrong")
#     print(j)
# # print(random.choice(word_list))
# for i in word_list:
#     print(i)


no_std=int(input ("enter the no of students who gived a Exam: "))
marks=[]
for i in range (1, no_std+1):
    def student (student_marks):
        marks.append(student_marks)
    x=int (input("Enter the marks of the student : "))
    student(x)
print (marks)
''' ////////////////////////'''



print("average marks of the students : ")
total=sum(marks)
average=total/len(marks)
print(f"average of the students marks is {average}")

# minimum and maximum got in exam
mini_marks=min(marks)
maxi_marks=max(marks)
print(f"Maximum marks got in exam is {maxi_marks}")
print(f"Minimum marks got in exam is {mini_marks}")

# No of student absent for exam
zero_count=marks.count(0)
print (f"{zero_count} students absent for tests")

# def most_frequent(marks):
#     return max (set(marks),key=list.count)
# markss=marks
# print(most_frequent(marks))
# 
import statistics
from statistics import mode 
def most_common(marks):
    return (mode(marks) )
markss=marks
print(most_common(markss))























