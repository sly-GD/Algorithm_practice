# iridescent_sly time:19:36 date:2024/5/28
try:
    while True:
        cnt0, cntX, ma0, maxX = map(int, input().split())
        maxX=min(maxX,cntX)
        ma0=min(ma0,cnt0)
        if ma0==0:
            print(maxX)
        elif maxX==0:
            print(ma0)
        elif ma0==0 and maxX==0:
            print(0)
        elif (cntX+1)*ma0<cnt0:
            print((cntX+1)*ma0+cntX)
        elif (cnt0+1)*maxX<cntX:
            print((cnt0+1)*maxX+cnt0)
        else:
            print(cnt0+cntX)
except:
    pass