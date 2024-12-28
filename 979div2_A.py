
def solve():
    for _ in range(test):
        l = int(input())
        ls = list(map(int, input().split()))
        bg = float('-inf')
        sm = float('+inf')

        for i in ls:
            if(i>bg):
                bg = i
            else:
                pass

        for i in ls:
            if(i<sm):
                sm = i
            else:
                pass

        a = 1
        fin_sum = 0
        while(a<l):
            fin_sum += bg-sm
            a+=1
        print(fin_sum)
test = int(input())

solve()

"""
    solved but could be more efficent way to solve this problem
    
"""