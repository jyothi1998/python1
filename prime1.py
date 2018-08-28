n=int(raw_input())
if (n==1):
     return false
 elif (n==2):
     return true;
 else:
     for x in range(2,1000):
          if(n % x==0):
          	  return false
       return true   	  
