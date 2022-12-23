n=int(input("ENTER NUMBER :"))
factorial=1
if n==0:
    print(" The factorial is :1")
elif n<0:
    print(" The factorial is not define ")
else:
  for i in range(1,n+1):
     factorial=factorial*i
  print("The factorial number is :",factorial)
  
