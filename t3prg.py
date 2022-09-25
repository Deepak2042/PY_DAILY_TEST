# l1=[]
# count=int(input("Enter the no. of marks: "))
# tot=0
# avg=0
# print("Enter the marks: ")
# for i in range(0,count):
#     val=int(input())
#     l1.append(val)
#
# for i in range(0,count):
#     tot+=l1[i]
#
# avg=tot/count
#
# if avg>=91 and avg<=100:
#     print("Grade: A1")
# if avg>=81 and avg<=90:
#     print("Grade: A2")
# if avg>=71 and avg<=80:
#     print("Grade: B1")
# if avg>=61 and avg<=70:
#     print("Grade: B2")
# if avg>=51 and avg<=60:
#     print("Grade: C1")
# if avg>=41 and avg<=50:
#     print("Grade: C2")
# if avg>33 and avg<=40:
#     print("Grade: D")
# if avg>=0 and avg<=33:
#     print("Grade: E")

#prg2-

# str=input("Enter the string: ")
# print("[",end='')
# for i in range(0,len(str)):
#     print(str[i],":",str.count(str[i]),end=',')
# print("]")

# #prg3-
num1=int(input("Enter the value: "))
num2=int(input("Enter the value: "))

grt=0
lcm=1

if num1<num2:
    grt=num1
else:
    grt=num2

while num1!=1 and num2!=1:
    for i in range(2,grt+1):
        print("i in loop: ",i)
        if num1%i==0:
            print(i)
            lcm*=i
            num1=int(num1/i)
        if num2%i==0:
            print(num1)
            num2=int(num2/i)
            print(num2)
print(lcm)
