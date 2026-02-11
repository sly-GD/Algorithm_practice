
res=0
for i in range(0-2020,2020+2020+1):
    for j in range(0-2020,2000+2020+1):
        if abs(i-0)+abs(j-0)<=2020 or abs(i-2020)+abs(j-11)<=2020 or abs(i-11)+abs(j-14)<=2020 or abs(i-2000)+abs(j-2000)<=2020:
            res+=1
print(res)

