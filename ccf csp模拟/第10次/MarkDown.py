# iridescent_sly time:20:08 date:2024/6/1
import sys
x=list(sys.stdin.read().split('\n'))
#print(x)
def biaoti(s):
    s = s.split(' ', 1)
    n=len(s[0])
    if "_" in s[1]:
        s1=s[1].split("_")
        # print(s1)
        t=s1[1]
        res='<h'+str(n)+'>'+s1[0]+'<em>'+t+"</em>"+s1[2]+'</h'+str(n)+'>'
        return res

    res ='<h'+str(n)+'>' +s[1] + '</h'+str(n)+'>'
    return  res

def duanluo(s):
    if "_" in s:
        s1=s.split("_")
        # print(s1)
        t=s1[1]
        res='<p>'+s1[0]+'<em>'+t+"</em>"+s1[2]+'</p>'
        return res
    res='<p>'+s+'</p>'
    return res
for i in x:
    if '#' in i:
        print((biaoti(i)))
    elif i=='':
        continue
    else:
        print(duanluo(i))

