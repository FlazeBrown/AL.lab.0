import time
t_start = time.perf_counter()
b = ['0','1']
def fib():
    global b
    if len(b) <= 45:
        s = int(b[-1]) + int(b[-2])
        b += [str(s)]
        return fib()
    else:
        return 0
fib()
f = open('input.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    g = line
f.close()
d = open('output.txt', 'w')
d.write(b[int(g)])
print('Время работы: %s секунд' % (time.perf_counter() - t_start))