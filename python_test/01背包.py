w=[0,1,2,4,2,5]
v=[0,5,3,5,3,2]

def ks(n,c):
    print('n=%d'%(n),'c=%d'%(c))
    print()
    if memo[n][c] != 0 :
        return memo[n][c]
    if n==0 or c==0:
        result=0
    elif w[n]>c:
        result=ks(n-1,c)
    else:
        temp1=ks(n-1,c)
        temp2=v[n]+ks(n-1,c-w[n])
        result=max(temp1,temp2)
        print(temp1,temp2,result)
    memo[n][c]=result
    for row in memo:
        print(row)
    print()
    return result
n=5;c=10
memo=[ [0]*(c+1) for i in range(n+1)]
print(ks(n,c))
