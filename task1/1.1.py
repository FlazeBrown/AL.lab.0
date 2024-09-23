a, b = map(int, input().split())
if a >= -10**9 and a <= 10**9 and b >= -10**9 and b <= 10**9:
    print(a + b)
else:
    print('Аргументы некорректны')