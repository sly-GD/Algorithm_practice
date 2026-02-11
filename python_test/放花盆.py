lst=input().split()
x=[]
for ele in lst:
    a,b=ele.split(",")
    x.append((int(a),int(b)))

rows={}
cols={}
maindiag={}
subdiag={}

for item in x:
    a,b=item[0],item[1]
    if a in rows:
        rows[a]+=1
    else :
        rows[a]=1
    if b in cols:
        cols[b]+=1
    else :
        cols[b]=1
    if a-b in maindiag:
        maindiag[a-b]+=1
    else :
        maindiag[a-b]=1
    if a+b in subdiag:
        subdiag[a+b]+=1
    else :
        subdiag[a+b]=1

print(rows,cols,maindiag,subdiag)
print(max(max(rows.values()),max(cols.values()),max(maindiag.values()),max(subdiag.values())))
