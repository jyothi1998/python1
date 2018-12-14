m=int(raw_input())
x=m
k=[]
while (m>0):
    a=int(float(m%2))
    k.append(a)
    m=(m-a)/2
string=""
for j in k[::-1]:
    string=string+str(j)
print string
