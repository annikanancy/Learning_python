"""for i in range (0,10,1):
    for j in range (0,5,1):
        print(i,j)"""

"""for i in range (1,11):
    for j in range (1,11):
        print(i, "X", j, "=", i*j)"""

n=int(input("Enter a number:"))
for i in range (1,n+1):
    print("Factors of", i, "are:")
    for j in range (1,i+1):
        if (i%j==0):
            print(j)