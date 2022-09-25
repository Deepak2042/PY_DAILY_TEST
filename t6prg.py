# grade=input("Enter the grade: ")
# sal=float(input("Enter the salary: "))
#
# bonus=0
#
# if sal>0 and (grade=="A" or grade=="B"):
#     if grade=='A':
#         if sal<10000:
#             bonus=(0.1*sal)+(0.02*sal)
#         else:
#             bonus=0.1*sal
#     if grade=='B':
#         if sal<10000:
#             bonus=(0.1*sal)+(0.02*sal)
#         else:
#             bonus=0.1*sal
#
# else:
#     if sal<0:
#         print("Salary can't be zero...!")
#     if grade>="C" and grade<="Z":
#         print("Grade doesn't exist...!!")
#
# print("Salary: ",sal)
# print("Bonus: ",bonus)
# print("Total to be paid: ",bonus+sal)


#prg2
l2=[]
l1=[]
temp=""
str=""
str1=input("Enter the string_1: ")
str2=input("Enter the string_2: ")

for i in str1:
    l1.append(i)
#print(l1)
pos=0

while pos<len(l1)-1:
    temp=l1[pos]
    l1[pos]=l1[pos+1]
    l1[pos+1]=temp
    print(str1)
    for i in l1:
        str2+=i
    l2.append(str2)
    pos+=2


for i in l2:
    if str2==i:
        print("S2 not scrumble of s1")
        break
    else:
        print("S2 is  scrumble of s1")
        break