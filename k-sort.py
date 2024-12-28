

def solve():
    l = int(input())
    lst = list(map(int, input().split()))
    
    if(l==1):
        print(0)
    else:
        coin = 1
        base = lst[0]
        for i in range(1,l):
            if(lst[i] < base):
                coin += base - lst[i]
                lst[i] = base
            else:
                base = lst[i]
                
        print(coin)




test = int(input())


for _ in range(test):
    solve()