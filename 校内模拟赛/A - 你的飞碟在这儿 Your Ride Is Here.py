# iridescent_sly time:19:13 date:2024/5/28
a = input()
b = input()
suma = 1
sumb = 1
for i in a:
    suma *=ord(i)-ord('A')+1
    #print(suma)
    suma %= 47
for i in b:
    sumb *= ord(i)-ord('A')+1
    #print(sumb)
    sumb %= 47
if sumb == suma:
    print('GO')
else:
    print('STAY')
