n=int(input())
fa=[0,0]+list(map(int,input().split()))

v=[0] + list(map(int,input().split()))

dep=[0] *(n+1)
dep_node = [[] for i in range(n+1)]
deep_max=0

for i in range(1,n+1):
    dep[i]=dep[fa[i]]+1
    deep_max=max(deep_max,dep[i])
    dep_node[dep[i]].append(i)
#print(dep)
for i in dep_node:
    print(i)

dp=[[0]*2 for i in range(n+1)]

state=[0,0,0]# [不选该层结点的最大值结点,选该层结点的最大值结点
                #,选该层结点非最大值同父最大值结点]
for i in range(deep_max,0,-1):
    print(f"第{i}层")
    for _ in dp:
        print(_)
    print()
    for j in dep_node[i]:
        
        dp[j][0]=max(dp[state[0]][0],dp[state[1]][1])
        if fa[state[1]]==j:
            dp[j][1]=v[j]+max(dp[state[0]][0],dp[state[2]][1])
        else:
            dp[j][1]=v[j]+max(dp[state[0]][0],dp[state[1]][1])
    state=[0,0,0]

    
    for j in dep_node[i]:
        print(state)
        if dp[state[0]][0]<dp[j][0]:
            state[0]=j
        if dp[state[1]][1]<dp[j][1]:
            state[1]=j

    for j in dep_node[i]:
        if fa[state[1]] != fa[j] and dp[state[2]][1]<dp[j][1]:
            state[2]=j
print(max(dp[1][0],dp[1][1]))
