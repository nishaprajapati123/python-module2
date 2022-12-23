#write a python function to reverses a string if its length is a multiple of 4
x=input("enter string:")
if len(x)%4==0:
   y=x[::-1]
   print(y)
else:
   print(x)
