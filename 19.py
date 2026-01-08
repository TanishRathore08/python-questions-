# fibonnaci series  0,1,2,3,5,8,13

n=int(input("enter the no :"))

a=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)