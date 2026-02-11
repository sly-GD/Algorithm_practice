arr=[]
for i in range(5):
    arr.append(input())
a,b=map(int,input().split())
arr[a-1],arr[b-1]=arr[b-1],arr[a-1]
for i in range(5):
    print(arr[i])
