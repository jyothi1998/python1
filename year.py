year = int(input("enter a year;"))
if(year%4==0):
    print("yes")
elif(year%400==0):
    print("yes")
else:
    print("no")
