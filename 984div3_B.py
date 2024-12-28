
def duplikeleri_kaldir(liste):
    görülen = set()
    tekil_liste = []

    for eleman in liste:
        if eleman not in görülen:
            tekil_liste.append(eleman)
            görülen.add(eleman)

    return tekil_liste

def solve():
    for _ in range(test):
        n,k = map(int, input().split())
        brand = []
        cost = []
        combined_list = []
        for _ in range(k):
            b,c = map(int, input().split())
            brand.append(b)
            cost.append(c)
            combined_list.append([b,c])

        h = duplikeleri_kaldir(brand)

        if(len(h) <= n):
            sum = 0
            for i in cost:
                sum +=i 
            print(sum)
        elif(len(h) > n):
            final_list = []

            for i in h:
                sum = 0
                for j in range(len(brand)):
                    if(combined_list[j][0] == i):
                        sum += combined_list[j][1]
                    else:
                        pass
                final_list.append(sum)

            
            final_list = sorted(final_list)
            last = 0
            for i in range(1,n+1):
                last += final_list[-i]

            print(last)









test = int(input())

solve()