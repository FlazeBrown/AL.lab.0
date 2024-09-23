import time
t_start = time.perf_counter()
b = ['0','1']
def fib(a):
    global b
    if len(b) != a:
        s = int(b[-1]) + int(b[-2])
        b += [str(s)]
        return fib(a)
    else:
        return 0
f = open('input.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    g = line
f.close()
d = open('output.txt', 'w')
fib(int(g) + 1)
d.write(str(int(b[-1]) % 10))
d.close()
print('Время работы: %s секунд' % (time.perf_counter() - t_start))
