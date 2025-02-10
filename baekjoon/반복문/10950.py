T = int(input()) # 5
pairs = []

for _ in range(T):
    A, B = map(int, input().split())
    pairs.append((A, B))

for A, B in pairs:
    print(A+B)
