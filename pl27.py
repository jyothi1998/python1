str=raw_input()
ans1=''
for x in str:
	if x.islower():
		ans1=ans1+x.upper()
	elif x.isupper():
		ans1=ans1+x.lower()
print(ans1)
