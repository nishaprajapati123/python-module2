x=int(input("enter value1:"))
y=int(input("enter value1:"))
z=int(input("enter value1:"))
n=x+y+z
#if(n==15 or n==16 or n==17 or n==18 or n==19 or n==20):
if n in range(15,20):
    print("return 20")
else:
    print("sum:",n)
