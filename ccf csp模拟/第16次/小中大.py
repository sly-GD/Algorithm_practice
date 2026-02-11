# iridescent_sly time:20:35 date:2024/5/19
n = int(input())
a = list(map(int, input().split()))
x, y, z = 0, 0, 0
if n % 2 == 0:
    z ='%.1f'% ((a[n // 2-1] + a[n // 2 ])/2)
    if z[-1]=='0':
        z=z[0:-2]
else:
    z=a[n//2]
x=a[0]
y=a[n-1]
if x>=y:
    print(x,z,y)
else:
    print(y,z,x)