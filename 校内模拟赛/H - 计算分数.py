# iridescent_sly time:20:07 date:2024/5/28
import fractions

a = input()

fenzi = []
fenmu = []
fuhao = []
for i in range(len(a)):
    if a[i] == '/':
        fenzi.append(int(a[i - 1]))
        fenmu.append(int(a[i + 1]))
    if a[i] == '+' or a[i] == '-':
        fuhao.append(a[i])
for i in range(len(fenzi) - 1):
    fuc_1 = fractions.Fraction(fenzi[i], fenmu[i])
    fun_2 = fractions.Fraction(fenzi[i + 1], fenmu[i + 1])
    if fuhao[i] == '+':
        x = fun_2 + fuc_1
    else:
        x = fuc_1 - fun_2
    fenzi[i + 1] = x.numerator
    fenmu[i + 1] = x.denominator
print(x)
