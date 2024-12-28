
def f(p):
    lst = []
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            lst.append(p[i:j])
    num = len(lst)
    return num
def solve():
    lst1 = []
    s = input()
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            lst1.append(s[i:j])   
    print(lst1)

    if()






test = int(input())

for _ in range(test):
    solve()