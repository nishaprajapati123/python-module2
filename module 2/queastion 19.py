#write a python program to find the first apperance of the substring 'not' and
#'poor' from a given string,if 'not' follows the 'poor' ,replace the whole 'not'
#...'poor' substring with 'good'.  return the resulting string.


x=input("enter string:")
xnot=x.find('not')
xpoor=x.find('poor')
if xpoor>xnot and xnot>0  and  xpoor>0:
    x=x.replace(x[xnot:(xpoor+4)],'good')
    print(x)
else:
    print(x)
