tuple1=(28.9,32.7,45.6,78,35,86.2,27.8,43,56,65)
arr=list(map(int,input().split()))
sum1=0
for i in range(len(arr)):
    sum1+=arr[i]*tuple1[i]
print("%.1f"%(sum1))
