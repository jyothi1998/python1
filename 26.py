m=raw_input()
list=[int(y) for y in raw_input().split()]
list.sort()
print " ".join(map(str,list))
