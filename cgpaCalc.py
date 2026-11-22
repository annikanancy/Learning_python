sub1=str(input("enter grade of sub1: "))
sub2=str(input("enter grade of sub2: "))
sub3=str(input("enter grade of sub3: "))
sub4=str(input("enter grade of sub4: "))
if sub1=="A+":
    gsub1=10
elif sub1=="A":
    gsub1=9
elif sub1=="B+":
    gsub1=8
elif sub1=="B":
    gsub1=7
elif sub1=="C+":
    gsub1=6
elif sub1=="C":
    gsub1=5
elif sub1=="D":
    gsub1=4
elif sub1=="E":
    gsub1=2
elif sub1=="F":
    gsub1=0
else: print("enter valid grades")

if sub2=="A+":
    gsub2=10
elif sub1=="A":
    gsub2=9
elif sub2=="B+":
    gsub2=8
elif sub2=="B":
    gsub2=7
elif sub2=="C+":
    gsub2=6
elif sub2=="C":
    gsub2=5
elif sub2=="D":
    gsub2=4
elif sub2=="E":
    gsub2=2
elif sub2=="F":
    gsub2=0
else: print("enter valid grades")

if sub3=="A+":
    gsub3=10
elif sub3=="A":
    gsub3=9
elif sub3=="B+":
    gsub3=8
elif sub3=="B":
    gsub3=7
elif sub3=="C+":
    gsub3=6
elif sub3=="C":
    gsub3=5
elif sub3=="D":
    gsub3=4
elif sub3=="E":
    gsub3=2
elif sub3=="F":
    gsub3=0
else: print("enter valid grades")

if sub4=="A+":
    gsub4=10
elif sub4=="A":
    gsub4=9
elif sub4=="B+":
    gsub4=8
elif sub4=="B":
    gsub4=7
elif sub4=="C+":
    gsub4=6
elif sub4=="C":
    gsub4=5
elif sub4=="D":
    gsub4=4
elif sub4=="E":
    gsub4=2
elif sub4=="F":
    gsub4=0
else: print("enter valid grades")

CGPA=5*(gsub1+gsub2+gsub3+gsub4)/(4*5)

print("Your CGPA is ", CGPA)



