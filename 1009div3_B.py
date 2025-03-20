import heapq
def solve():
    length = int(input())
    input_str = input().strip()
    lst = list(map(int, input_str.split()))
    lst.sort()
    heapq.heapify(lst)

    while len(lst) > 1:
        
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        new_num = first + second - 1
        heapq.heappush(lst, new_num)

    
    print(lst[0])
     

test = int(input())
for i in range(test):
    solve()
