#lab problem 1
#Programs on selection and iteration operations:-
''' If The num is odd you have to find its factorial or the num even check that number is palindrome or not... '''
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)

num=int(input('Enter Number: '))
if num%2==0:
    print("The num is even")
    rev=0
    non=num
    while(num>0):
        last=num%10
        rev=rev*10+last
        num=num//10
    if (rev==non):
        print("The given number is palindrome")
    else:
        print("The given number is not palindrome")
else:
    print("The factorial of a number is",factorial(num))
    count=0
    n=factorial(num)
    while(n>0):
        n=n//10
        count=count+1
    print("Count of numberS: ",count)