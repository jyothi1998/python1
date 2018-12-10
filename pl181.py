def isSum(n,x,y):
    if x<y:
        y,x=x,y
    while n>=0:
        if n%x==0:
            return True
        n-=y
    return False
        
n = int(input())
if isSum(n,3,7):
    print("yes")
else:
    print("no")
