s1=input("Enter the string-1: ")
s2=input("Enter the string-2: ")

l1=list(s1.split())
l2=list(s2.split())

for i in range(0,len(l1)):
    if l1[i] not in l2:
        print(l1[i],end=' ')
print(" ")
for i in range(0,len(l2)):
    if l2[i] not in l1:
        print(l2[i],end=' ')