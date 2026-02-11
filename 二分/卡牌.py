# iridescent_sly time:17:47 date:2024/5/2


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def check(x):
    global m
    op = m
    #print("x={}".format(x))
    for i in range(len(a)):
        if x - a[i]>b[i] :
            #print(op,x-a[i])
            return False

        # print("这次op减了{} ，op={}".format(x-a[i],op))
        op -= max((x - a[i]),0)

    if op<0:
        return False
    else:
        return True


inf = 0x3f3f3f3f
r = inf
l = 0

while (l <= r):
    #print(l,r)
    mid = (l + r) // 2
    if check(mid):
        ans=mid   #要保存中间值，这个才是答案，l，r会进入下一轮发生变化
        l = mid + 1
    else:
        r = mid - 1
print(ans)
