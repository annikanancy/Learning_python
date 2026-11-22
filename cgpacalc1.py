n=int(input("Enter number of subjects: "))
sub=list(map(str,input("Enter subject code: ").split()))
credit=list(map(int,input("Enter subject credit: ").split()))
grade=list(map(str,input("Enter subject grade: ").split()))
grade_points=[]
for i in range (0, n, 1):
    if grade[i]=="A+":
        grade_points.append(10)
    elif grade[i]=="A":
        grade_points.append(9)
    elif grade[i]=="B+":
        grade_points.append(8)
    elif grade[i]=="B":
        grade_points.append(7)
    elif grade[i]=="C+":
        grade_points.append(6)
    elif grade[i]=="C":
        grade_points.append(5)
    elif grade[i]=="D":
        grade_points.append(4)
    elif grade[i]=="E":
        grade_points.append(2)
    else: grade_points.append(0)
    sum_cr = 0
for i in range (0, n):
    grade_points[i]*=credit[i]
    sum_cr+=credit[i]
sum_gp=0
for i in range (0,n):
    sum_gp+=grade_points[i]
CGPA = sum_gp/sum_cr
print("Your CGPA is ", CGPA)

    
       