N, M = [int(x) for x in input().split()]
Anya = set()
Borya = set()
for i in range(N):
    x = int(input())
    Anya.add(x)
for i in range(M):
    x = int(input())
    Borya.add(x)
set1 = Anya & Borya
set2 = Anya - Borya
set3 = Borya - Anya
print(len(set1))
print(*sorted(set1))
print()
print(len(set2))
print(*sorted(set2))
print()
print(len(set3))
print(*sorted(set3))