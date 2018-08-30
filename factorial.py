n = int(raw_input())
fact = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
     print (n)
else:
   for i in range(1,n + 1):
       fact = fact*i
   print(fact)
