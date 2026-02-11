# iridescent_sly time:15:35 date:2024/5/11
n = int(input())
mk = {}
bk = ['L', 'O']


def dfs(s):
    if s in mk:
        return mk[s]
    if 'LO*' in s or 'L*L' in s or '*OL' in s:
        mk[s] = 1
        return 1
    if '*' not in s and 'LOL' not in s:
        mk[s] = 0
        return 0
    draw = 0
    for i, c in enumerate(s):
        if c == '*':
            for _ in bk:
                s = s[:i] + _ + s[i + 1:]
                if 'LO*' in s or "L*O" in s or '*OL' in s:
                    s = s[:i] + '*' + s[i + 1:]
                    continue
                now = dfs(s)
                s = s[:i] + '*' + s[i + 1:]
                if now == -1:
                    mk[s] = 1
                    return 1
                elif now == 0:
                    '''不能在这里记录返回，还要继续搜索后面情况'''
                    draw = 1
    if draw == 1:
        mk[s] = 0
        return 0
    mk[s] = -1
    return -1


for i in range(n):
    s = input()
    #print(mk)
    print(dfs(s))
