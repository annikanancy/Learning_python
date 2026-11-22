chasma=[1,2,3,4]
"""for i in range (0,4):
    print(chasma[i])"""
"""add=0
for i in range (0,4):
    add+=chasma[i]
print(add)"""

#max element
"""maxm=float("-inf")
for i in range (0,4):
    if(chasma[i]>maxm):
        maxm = chasma[i]
print("max element is ", maxm)"""

#min element
"""minm=float("inf")
for i in range (0,4):
    if(chasma[i]<minm):
        minm=chasma[i]
print("Min Element Is:", minm)"""

#print elements at even indices
"""for i in range (0,4,2):
    print(chasma[i])"""
#print(chasma[0:4:2])

#count even number
"""annika=list(map(int,input().split()))
count=0
for i in range (0,len(annika),1):
    if annika[i]%2==0:
        count+=1
print("no. of evens are",count)"""

#check if element is present
"""annika=[5,4,5,2,82,79,16]
target=int(input("Enter target:"))
present = False
for i in range (0,7):
    if annika[i]==target:
        present = True
if(present):
    print("present")
else:
    print(absent)"""


annika=list(map(int,input().split()))
even=[]
odd=[]
for i in range (0,len(annika),1):
    if annika[i]%2==0:
        even.append(annika[i])
    else: odd.append(annika[i])    
print(even)
print(odd)
    
