# write a program to find the list of prime numbers using class and object.

class prime_number:
    def find(self,a,b):
        for n in range(a,b+1):
            if n>1:
                for i in range(2,n):
                    if n % i == 0:
                        break
                else:
                    print(n,end=" ")

obj = prime_number()
obj.find(10,25)
