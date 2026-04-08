a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>=b and a>=c:
    print("highest number is:",a)
elif b>=a and b>=c:
    print("highest number is:",b)
else:
    print("highest number is:",c)
