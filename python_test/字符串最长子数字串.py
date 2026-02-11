s=input()

def isNumber(n):
    if n>=chr(ord('0')) and n<=chr(ord('9')):
        return True
    return False
cnt=0
res=0
for i in s:
    if isNumber(i):
        cnt+=1
    else :
        cnt=0
    res=max(res,cnt)
print(res)
print(chr(ord('0')),chr(ord('9')))
