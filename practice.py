"""Armstrong Number"""
"""n=int(input("Enter n: "))
sum=0
count=0
original=n
x=n
while x!=0:
    count+=1
    x=int(x/10)
while n>0:
    sum+=(n%10)**count
    n=int(n/10)
if (original==sum):
    print("ARMSTRONG NUMBER!")"""

"""#Perfect Number
n=int(input("Enter n: "))
divisor=0
i=1
while i<n:
    if n%i==0:
        divisor+=i
    i+=1
if divisor==n:
    print("PERFECT NUMBER!")"""

#prime number
"""n=int(input("Enter a number: "))    
prime=True
i=2
while i<n:
    if n%i==0:
        prime=False
    i+=1
if prime: print("Prime")"""

"""n=int(input("Enter n: "))
a=int(input("Enter a: "))
b=int(input("Enter b: "))
i=a
while i<=b:
    if(i%n==0):
        print(i)
    i+=1"""

"""n=int(input("Enter a number: "))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1    """

#hcf
"""a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
while b!=0:
    a, b = b, a%b
print("HCF =",a)"""

#LCM
"""a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
product=a*b
while b!=0:
    a, b = b, a%b
LCM=product/a
print(LCM)"""

#Fibonacci Series
"""n=int(input("Enter number of terms: "))
a=0
b=1
sum=a
for i in range (0, n, 1):
    print(a, end=" ")
    a,b=b,a+b
    sum+=a
print()
print("Sum of Fibonacci Series upto",n, "terms is", sum)"""

#smallest digit & largest digit
n=int(input("Enter a number: "))
x=n
small=float('inf')
large=float('-inf')
while x>0:
    small=min(small, x%10)
    large=max(large, x%10)
    x=int(x/10)
print("Smallest digit is:", small) 
print("Largest digit is:", large)  




