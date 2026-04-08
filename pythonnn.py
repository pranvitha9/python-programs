Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=int(input("Enter First number"))
Enter First number10
b=int(input("Enter second Number"))
Enter second Number19
c=int(input("Enter third number"))
Enter third number4
print("Total=",a+b+c)
Total= 33
print("Average=",a+b+c/3)
Average= 30.333333333333332
a=float(input("Enter first number:"))
Enter first number:2.0
b=float(input("Enter second number :"))
Enter second number :9.0
print("Choose Operation : + - /  *")
Choose Operation : + - /  *
>>> op=input("Enter operation: ")
Enter operation: +
>>> if op == '+' :
...     print("Result :",a+b)
... elif op == '-' :
...     print("Result :",a-b)
... elif op =='/' :
...     print("Result :",a/b)
... elif op == '*' :
...     print("Result :",a*b)
... else :
...     print("Invalid operator")
... 2.0+9.0
SyntaxError: invalid syntax
>>> 2.0+9.0
11.0
>>> +
SyntaxError: invalid syntax
>>> p=float(input("Enter principal amount :"))
Enter principal amount :1000
>>> r=float(input("Enter rate of Interest:"))
Enter rate of Interest:5
>>> t=float(input("Enter time(in years):"))
Enter time(in years):2
>>> si=(p*r*t)/100
>>> print("Simple Interestcis:",si)
Simple Interestcis: 100.0
>>> a=10
>>> b=20
>>> temp=a
>>> a=b
>>> b=temp
>>> print("a=",a)
a= 20
>>> print("b=",b)
b= 10
>>> num=float(input("Enter a number:"))
Enter a number:4
>>> square = num*num
>>> print("Square =",square)
Square = 16.0
>>> a=int(input("enter number:"))
enter number:4
>>> print(a**0.5)
2.0
