x,y,z=map(int,raw_input().split())
if(x>y and x>z):
  num1=x
  num2=y
  num3=z
elif(y>z and y>x):
  num1=y
  num2=x
  num3=z
else:
  num1=z
  num2=x
  num3=y
num1=num1**2
num2=num2**2
num3=num3**2
num4=num2+num3
if(num1==num4):
  print("yes")
else:
  print("no")
