# write a program to check leap year

year = int(input("enter the year:"))

# leap year - 366 day  -  once in four year

if ( year%400==0 ) and (year%100==0):
    print(year,"year is a leap year")

elif (year%4==0) and (year%100!=0):
    print(year,'year is a leap year')

else:
    print(year,'year is not leap year')