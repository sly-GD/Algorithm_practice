# iridescent_sly time:16:10 date:2024/5/5
n = int(input())
s = input()
a = []
for i in s:
    a.append(int(i))


def xiaolan():
    global a
    x = 1
    for i in range(1, len(a)):
        if a[i - 1] == a[i]:
            a.pop(i)
            break
        if i == len(a) - 1:
            a.pop()
            break

    return


def xiaohong():
    global a
    if len(a) == 1:
        a.pop(0)
        return
    for i in range(1,len(a)):
        if i == len(a):
            break
        if a[0] == a[i]:
            a[i]=-1
            continue
        break
    while -1 in a:
        a.remove(-1)
    a.pop(0)
    return


ans = 0
while len(a) != 0:
    xiaolan()
    #print(a)
    xiaohong()
    #print(a)
    ans += 1
print(ans)
