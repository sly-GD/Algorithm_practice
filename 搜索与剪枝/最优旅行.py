# iridescent_sly time:13:01 date:2024/5/12
import sys

minTime = sys.maxsize
totaltime = 0
vis = [0] * 25

'''
class Node:
    def __init__(self, des, startt, endt, cost):
        self.e = des
        self.starttime = startt
        self.endtime = endt
        self.cost = cost
'''

G = [[] for i in range(25)]  # 以出发点为单位存储班次信息

m = {
    '上海': 1, '广州': 2, '长沙': 3, '西安': 4, '杭州': 5, '济南': 6, '成都': 7, '南京': 8, '昆明': 9, '郑州': 10,
    '天津': 11, '太原': 12, '武汉': 13, '重庆': 14, '南昌': 15, '长春': 16, '沈阳': 17, '贵阳': 18, '福州': 19,
    '北京': 20
}


def dfs(s, endt, len):
    print(s)
    global minTime, totaltime, vis
    if len > 0 and s == 20:
        flag = all(vis[i] == 1 for i in range(1, 21))
        vis[20] = 0  # 北京是可以去多次的，可以经过
        if flag:
            minTime = min(minTime, totaltime)
        return
    for r in G[s]:
        if vis[r[0]] == 0:
            vis[r[0]] = 1
            temp = totaltime
            totaltime += r[3]
            if s != 20 and r[1] > endt:
                totaltime += r[1] - endt
            if s != 20 and r[1] < endt:
                totaltime += r[1] - endt + 1440
            if s == 20:
                if r[1] > 720:
                    totaltime += r[1] - 720
                else:
                    totaltime += r[1] - 720 + 1440
            if totaltime > minTime:
                totaltime = temp
                continue
            dfs(r[0], r[2], len + 1)
            vis[r[0]] = 0
            totaltime = temp


for i in range(132):
    line = input().split()
    src = line[1]
    des = line[2]
    s = line[3]
    t = line[4]

    if src not in m or des not in m:
        print('Invalide city name', src, 'or', des)
        continue
    a = int(s[:2]) * 60 + int(s[3:])
    b = int(t[:2]) * 60 + int(t[3:])
    cost = b - a if b > a else b - a + 1440

    G[m[src]].append([m[des], a, b, cost])
dfs(20, 0, 0)
minTime += 1440 * 19
print(minTime)
