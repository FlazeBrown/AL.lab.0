f = open('input.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    g = line
f.close()
s = g.split()
if int(s[0]) <= 10**9 and int(s[0]) >= -10**9 and int(s[1]) <= 10**9 and int(s[1]) >= -10**9:
    r = open('output.txt', 'w')
    h = int(s[0]) + int(s[1])**2
    r.write(str(h))
    r.close()