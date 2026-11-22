"""n=int(input())  
mul=1
x=n
while x>0:
    mul*=int(x%10)
    x=int(x/10)
print(mul)"""

"""n=int(input())
count=0
x=n
while x>0:
    count+=1
    x=int(x/10)
print(count)"""

"""n=int(input())
rev=0
x=n
while x>0:
    rev*=10
    rev+=x%10
    x=int(x/10)
print(rev)
if n==rev: print("palindrome")
else: print("not palindrome")"""

n=int(input("Enter a number:" ))
i=1
while i<=n:
    print(i**3)
    i+=1
