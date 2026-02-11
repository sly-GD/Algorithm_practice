while True:
    try:
        x=input()
        if not x:
            break
        y=0
        for i in range(len(x)):
           if x[i].isdigit():
               y+=int(x[i])
        print(y)
    except:
        break
##注意事项:有一个测试样例第一位就是EOF，
##不知道是不是网站系统更新了，之前通过的老代码现在重新用反而通过不了了，
##就是因为这个测试样例，加一个try-except检查EOF错误就行
