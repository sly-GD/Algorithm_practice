v=int(input())
a=[]
st=[0]

def dfs(u,last):
        if u==n:
            return True
        for i in range(n):
            if st[i]==0 and a[i][0]+a[i][1]>=last:
                st[i]=1
                if dfs(u+1,max(last,a[i][0])+a[i][2]):
                    #print("good")
                    return True
                st[i]=0
        return False
while v>0:
    n=int(input())
    a=[]
    st=[0]*n
    for i in range(n):
        a.append(list(map(int,input().split())))
    
    if dfs(0,0):
        print("YES")
    else:
        print("NO")
    v-=1
