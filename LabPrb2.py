#lab problem 2
#strings and its operations
'''Get 2 input from user then print << Yes or No >> whether the string 2 can be
 obtained from string 1 by deletion of none , one or more characters '''

str1=input()
str2=input()
str3=''
temp=0
len1=len(str1)
len2=len(str2)
for iter1 in range(0,len2):
    for iter2 in range(temp,len1):
        if (str2[iter1]==str1[iter2]):
            str3=str3+str[iter2]
            temp=iter2+1
            break
if (str2==str3):
    print("Yes")
else:
    print("no")