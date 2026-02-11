'''n=int(input())
while n:
    list1=input().split()
    if list1[0]=="Rock":
        if list1[1]=="Scissors":
            print("Player1")
        elif list1[1]=="Paper":
            print("Player2")
        else :
            print("Tie")
    if list1[0]=="Scissors":
        if list1[1]=="Paper":
            print("Player1")
        elif list1[1]=="Rock":
            print("Player2")
        else :
            print("Tie")
    if list1[0]=="Paper":
        if list1[1]=="Rock":
            print("Player1")
        elif list1[1]=="Scissors":
            print("Player2")
        else :
            print("Tie")
    n-+1
'''
list1=['Rock','Scissors','Paper']
def judge(s1,s2):
    if s1==s2:
        print('Tie')
    elif (s1==list1[0] and s2==list1[1]) or (s1==list1[1] and s2==list1[2]) or (s1==list1[2] and s2==list1[0]):
        print('Player1')
    else :
        print('Player2')
n=int(input())
for i in range(n):
    s=input().split()
    judge(s[0],s[1])
