name=input("Enter name: ")
course=input("Enter course name: ")
section=input('Enter section: ')
pyhton=float(input('Enter python marks: '))
c=float(input('Enter c++ marks: '))
java=float(input('Enter java marks: '))
php=float(input('Enter php marks: '))

total=pyhton+java+c+php
percentage=total/4

print("\n-----------------Printing result---------------------")
print("name:",name )
print("course: ",course)
print('Section: ',section)
print('percentage: ',percentage,'%')
