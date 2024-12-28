

def solve():
    n, k = map(int, input().split())
    scale = []
    new_n = n // k   
    for _ in range(n):
        scale.append(input())
    
    new_scale = [] 
    for i in range(new_n):
        new_scale.append(scale[i*k])            

    ssc = []
    for j in new_scale:
        p = ''
        for e in range(new_n):
             p+= j[e*k]
             
        ssc.append(p)


    for o in ssc:
        print(o)



test = int(input())

for _ in range(test):
    solve()
"""
    SOLVEEEEEEEEEED!
"""