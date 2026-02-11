ans=0
big=[1,3,5,7,8,10,12]

a="5 6 8 6 9 1 6 1 2 4 9 1 9 8 2 3 6 4 7 7 5 9 5 0 3 8 7 5 8 1 5 8 6 1 8 3 0 3 7 9 2\
7 0 5 8 8 5 7 0 9 9 1 9 4 4 6 8 6 3 3 8 5 1 6 3 4 6 7 0 7 8 2 7 6 8 9 5 6 5 6 1 4 0 1\
0 0 9 4 8 0 9 1 2 8 5 0 2 5 3 3"
a=a.split()

b=""
for i in a:
    b=b+str(i)


flg=b.find('2')
flg1=b.find("0",flg+1)
flg2=b.find("2",flg1+1)
flg=b.find("3",flg2+1)
print(flg)


for m in range(1,13):
    for d in range(1,32):
        #print(m,d)
        if m in big:
            pass
        elif m==2:
            if d>28:
                break
        else:
            if d>30:
                break

        s=f"{m:02}{d:02}"
        #print(s[0])
        f=b.find(s[0],flg+1)
        #$print(f)
        if f==-1:
            continue
        f1=b.find(s[1],f+1)
        if f1==-1:
            continue
        f2=b.find(s[2],f1+1)
        #print("here")
        if f2==-1:
            continue
        f3=b.find(s[3],f2+1)
        if f3==-1:
            continue
        ans+=1
print(ans)
