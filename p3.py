m=int(raw_input())
rev=0
while(m>0):
    remainder=m%10
    rev=rev*10+remainder
    m=m/10
print rev    
