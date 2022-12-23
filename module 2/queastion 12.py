# write a python program to calculate the length of string

x=input("enter a string:")
c=0
n=0
sp=0
for i in x:
    c=c+1
if i.isspace():
        sp=sp+1
if i.isnumeric():
        n=n+1
total=c+sp+n
print("total:",total)
#count=0
#for i in x:
 #   count =count+1
#print("count:",count)



    

 
