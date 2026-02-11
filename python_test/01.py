a=[i for i in range(26)]
print(a)

s="adef"
v=list(s)
sum1=0
for i in range(len(s)):
    sum1+=a[ord(s[i])-ord('a')]

print(sum1)
