#creation
annika = [1,2,3,4,[1,2,3],"udit",2.999]
print(annika)

annika.append(45) #adds 45 to end of list
print(annika)
annika.insert(0,4) #insert 4 at idx 0
print(annika)
annika.extend([10,11,12])
print(annika)
annika.remove("udit")
print(annika)
annika.pop(3)
print(annika)
del annika[0]
print(annika)
del annika[6:8]
print(annika)
print(len(annika))

print([1,2,3] in annika)

#slicing
print(annika[3:7:2])

annika = [2,1,7,2,1,6,0,9,5]
print(annika)

annika.sort()
print(annika)

annika.sort(reverse=True)
print(annika)

annika.reverse()
print(annika)

print(annika.count(1))

print(annika.index(2))

#input_list
"""udit = list(map(int,input().split()))
print(udit)"""