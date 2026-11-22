a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
product=a*b
while b!=0:
    a,b=b,a%b
print("HCF is:",a)
print("LCM is:",int(product/a))
