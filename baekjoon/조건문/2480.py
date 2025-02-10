first, second, third = map(int, input().split())

sameThree = first == second == third
sameTwo = (first == second) or (second == third) or (first == third)
diff = first != second and second != third and first != third

if sameThree:
    print(10000 + first * 1000)
elif sameTwo:
    if first == second:
        print(1000 + first * 100)
    elif second == third:
        print(1000 + second * 100)
    elif first == third:
        print(1000 + third * 100)
else:
    print(max(first, second, third) * 100)
    