# Draw a Square


def solve():
    square = list(map(int, input().split()))
    square = list(set(square))
    if(len(square) == 1):
        print("yes")
    else:
        print("no")



test = int(input())

for i in range(test):
    solve()