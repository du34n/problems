
def solve():
    l = int(input())
    s = input()
    indis = 0
    i = 0
    while('B' != s[i]):
        i+=1
    j = len(s)-1
    while('B' != s[j]):
        j-=1
        
    if(j==i):
        print(1)
    else:
        print(j-i+1)

test = int(input())
for _ in range(test):
    solve()


"SOLVED!!!"