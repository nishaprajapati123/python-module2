#write a python program to get a single string from two given string,separated
#by a space and swap the first two characters of each string.


str1=input("enter string:")
str2=input("enter string:")
x=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],x)
print(str1, "  " ,str2)
