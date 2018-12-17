num1=int(raw_input())
ans=0
while(num1!=0):
	temp=num1%10
	ans=ans+(temp*temp)
	num1=num1//10
print(ans)
