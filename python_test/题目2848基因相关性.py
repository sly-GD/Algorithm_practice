n=float(input())
a,b=input(),input()
x=0
for i in range(len(a)):
    if a[i]==b[i]:
        x+=1
if x/min(len(b),len(a))>=n:
    print("yes")
else:
    print("no")
