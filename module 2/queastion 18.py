#write python program to add 'ing' at the end of a given string (length should
#be at least3).if the given string  already ends with 'ing' then add 'ly'instead
#if the string length of the given string is  less than 3,leave it unchanged.



x=input("enter string:")
if len(x)<3:
    print(x)
elif x[-3:]=='ing':
    print(x + "ly")
else:
    print(x + "ing")
