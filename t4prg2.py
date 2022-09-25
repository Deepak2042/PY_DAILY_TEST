str=input("Enter the text: ")

text=list(str.split())
count=0

for i in range(0,len(text)):
    if text[i]=="a" or text[i]=="the" or text[i]=="an":
        count+=1

print("Articles count: ",count)