
# #python progrm to perform opertions on matrix
# #addition of two matrices
# mat1=[[1,6],[1,5]]
# mat2=[[2,4],[3,6]]
# mat3=[[0,0],[0,0]]
# for i in range(0,2):
#     for j in range(0,2):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]
# print("addition of two matrices")
# for r in mat3:
#     print(r)

# #substraction of two matrices

# for i in range(0,2):
#     for j in range(0,2):
#         mat3[i][j]=mat1[i][j]-mat2[i][j]
# print("substraction of two matrices")
# for r in mat3:
#     print(r)

# #multiplications of two matrices

# for i in range(0,2):
#     for j in range(0,2):
#         mat3[i][j]=mat1[i][j]-mat2[i][j]
# print("multiplication of two matrices")
# for i in range(len(mat1)):
#     for j in range(len(mat2[0])):
#         for k in range(len(mat2)):
#             mat3[i][j]=mat3[i][j]+(mat1[i][j]*mat2[k][j])
# for r in mat3:
#  print(r)

import turtle

# Set the background color
turtle.bgcolor("lightblue")

# Create a turtle object
doraemon = turtle.Turtle()

# Set the turtle shape
doraemon.shape("turtle")

# Set the turtle color
doraemon.color("blue")

# Set the turtle speed
doraemon.speed(10)

# Draw Doraemon's head
doraemon.begin_fill()
doraemon.circle(100)
doraemon.end_fill()

# Move the turtle to the position for the left ear
doraemon.penup()
doraemon.goto(-80, 120)
doraemon.pendown()

# Draw Doraemon's left ear
doraemon.begin_fill()
doraemon.circle(20)
doraemon.end_fill()

# Move the turtle to the position for the right ear
doraemon.penup()
doraemon.goto(80, 120)
doraemon.pendown()

# Draw Doraemon's right ear
doraemon.begin_fill()
doraemon.circle(20)
doraemon.end_fill()

# Move the turtle to the position for the mouth
doraemon.penup()
doraemon.goto(0, 40)
doraemon.pendown()

# Draw Doraemon's mouth
doraemon.left(45)
doraemon.forward(50)
doraemon.right(90)
doraemon.forward(50)
doraemon.left(45)

# Move the turtle to the position for the left eye
doraemon.penup()
doraemon.goto(-40, 120)
doraemon.pendown()

# Draw Doraemon's left eye
doraemon.begin_fill()
doraemon.circle(10)
doraemon.end_fill()

# Move the turtle to the position for the right eye
doraemon.penup()
doraemon.goto(40, 120)
doraemon.pendown()

# Draw Doraemon's right eye
doraemon.begin_fill()
doraemon.circle(10)
doraemon.end_fill()

# Hide the turtle
doraemon.hideturtle()

# Prevent the window from closing immediately
turtle.exitonclick()
