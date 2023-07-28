list1=['A','B','C','D','X'] #CRICKET
list2=['E','F','A','C','Y'] #BADMINTON
list3=['B','D','E','F','Z'] #FOOTBALL
r1=[]
r2=[]
a=[]
r3=[]
b=[]
r4=[]
def func1():
for i in list1:
for j in list2:
if(i==j):
r1.append(i)
print("List ofstudents who play both cricket and badminton:",r1)
func1()
def func2():
for i in list1:
f=0
for j in list2:
if(i==j):
f=f+1
if(f==0):
r2.append(i)
for j in list2:
f=0
for i in list1:
if(i==j):
f=f+1
if(f==0):
r2.append(j)
print("List ofstudents who play either cricket or badminton but not both:",r2)
func2()
def func3():
for i in list1:
for k in list3:
if(i==k):
a.append(i)
for j in list2:
for k in list3:
if(j==k):
a.append(j)
for k in list3:
f=0
for l in a:
if(k==l):
f=f+1
if(f==0):
r3.extend(k)
print("List of students who neither play cricket nor badminton:",r3)
print("Number ofstudents who neither play cricket nor badminton:",len(r3))
func3()
def func4():
for i in list1:
for k in list3:
if(i==k):
b.append(i)
for l in b:
f=0
for j in list2:
if(l==j):
f=f+1
if(f==0):
r4.append(l)
print("List of students who play cricket and football but not badminton:",r4)
print("Number ofstudents who play cricket and football but not badminton:",len(r4))
func4()