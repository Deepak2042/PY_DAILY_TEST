l1=[]
l3=[]
l2=[]
ele=int(input("Enter the no.elements: "))
print("Enter the value: ")
for i in range(0,ele):
    val=input()
    l1.append(val)
for i in l1:
    word1=i
    for j in l1:
        word2=j
        for k in word1:
            if k in word2:
                l2.append(word2)
    
    l3.append(l2)
    l2.clear()
for i in range(0,len(l2)):
    for j in range(0,len(l2)):
        if(l2[i]<l2[j]):
            temp=l2[i]
            l2[i]=l2[j]
            l2[j]=temp
                
print(set(l2))
print(l3)
            
