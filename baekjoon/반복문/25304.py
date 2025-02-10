X = int(input()) # 총 금액
N = int(input()) # 물건 개수
pairs = []
pairsPriceResult = 0


# 1. N 만큼 a, b를 받음
# 2. a, b를 pair로 받고 list로 저장
# 3. 각 pair a, b 곱셈 결과 후 더한 총 값을 X와 비교

for _ in range(N):
    a, b = map(int, input().split()) # a: 가격, b: 개수
    pairs.append([a, b]) # list 추가

for a, b in pairs:
    pairsPriceResult += a * b # a와 b를 곱해서 result에 더함

if pairsPriceResult == X:
    print("Yes")
else:
    print("No")

