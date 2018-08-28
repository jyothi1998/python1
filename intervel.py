lower,upper=map(int,raw_input().split())
for x in range(lower,upper+1):
    if(x%2!=0) and x!=1:
        print(x)
