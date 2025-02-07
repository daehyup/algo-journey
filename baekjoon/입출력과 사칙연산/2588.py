A = int(input())
B = int(input())

arr = [int(digit) for digit in str(B)][::-1] # 역순 저장 [::-1]

for num in arr:
    print(num * A) 

print(A * B)  
