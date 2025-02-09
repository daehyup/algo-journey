hour, minute = map(int, input().split())

if hour == 0:
    hour = 24

hour -= 1
minute += 15

print(hour, minute)