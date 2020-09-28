y=input("Enter number of required digits:")
n=int(y)
a=0
b=1
print(a)
print(b)
for i in range(1,n//2):
    a=a+b
    b=a+b
    print(a)
    print(b)
if n%2!=0:
    a=a+b
    print(a)
