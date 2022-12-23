#write a python program to get a string made of the first 2 and the last 2 char
#from a given a string .if the string length is less than 2, return instead of
#the empty string.

x=input("enter string:")
if len(x)<2:
  print("empty string")
else:
  y = x[0:2] + x[-2:]
#z= x[-2:]
  print(y)
