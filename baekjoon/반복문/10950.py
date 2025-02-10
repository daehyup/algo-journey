T = int(input()) # 5
pairs = []

for _ in range(5):
    A, B = map(int, input().split())
    pairs.append((A, B))

for A, B in pairs:
    print(A+B)
