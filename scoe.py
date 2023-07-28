# str1=input("enter the string ")
# print(str1[:-1])
# print(str1[-1:1])
# a=( reverse==trure)sort()
# if (str1[0:]==str1[:-1]) :
#     print("enter string is palindrom")
# else:
#     print("given string is not palindrom ")
''' write a python program to find a sum of n natural numbers '''
# number =int(input("enter the no which you have to get addtion of that numbers"))
# num=0
# for i in range (0,number+1):
#     num+=i
# print(num)
# while num<number:
#     num=num+1
# a=9
# l=0
# print(a,l=l,a )
# a=str(input("Enter the string "))
# str2=a[::-1]
# if a==str2 :
#     print("palindrome")
# else:
#     print("not palidrome")



''' experiment no 7 of PPS'''

class Employee:
    totalEmployee=0
    males=0
    females=0
    
    def __init__(self,name,designation,gender,doj,salary):
        self.name=name
        self.designation=designation
        self.gender=gender
        self.doj=doj
        self.salary=salary
        Employee.totalEmployee+=1
        if self.gender=='M':
            Employee.males+=1
        else:
            Employee.females+=1
            
    @staticmethod
    def totalEmployeeCount():
        return Employee.totalEmployee
    @staticmethod
    def genderCount():
        print("No.of males:",Employee.males)
        print("No.of Femalesll:l",Employee.females)
        
    def isSalaryGreater10000(self):
        if self.salary>'10000':
            return True
        else:
            return False
    def isAsstManager(self):
        if self.designation=="Asst Manager":
            return True
        else:
            return False

def create():
    name=input("Name:")
    designation=input("Designation: ")
    gender=input("Gender(M/F):")
    doj=input("Enter Date of Joining: ")
    salary=input("Salary:")
    emp=Employee(name,designation,gender,doj,salary)
    return emp
    
def main():
    emp_list=[]
    while(1):
        print("1.Create Employee\n2.Total Employees\n3.Gender count\n4.Employee with salary>10000\n5.Asst Managers")
        choice=int(input("Enter your choice:"))
        if choice==1 :
            emp_list.append(create())
        elif choice==2:
            print("Total No. of Employees: ", Employee.totalEmployeeCount())
        elif choice==3:
            print(Employee.genderCount())
        elif choice==4:
            for emp in emp_list:
                if emp.isSalaryGreater10000():
                    print("Employee having salry than 10000: ", emp.name)
        elif choice==5:
            for emp in emp_list :
                if emp.isAsstManager():
                    print("Employee with designation as Asst Manager: ",emp.name)
        else:
            print("Invalid choice")
            
if __name__=='__main__':
    main()
                   
            
                


