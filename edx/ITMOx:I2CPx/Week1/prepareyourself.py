# ti = how much ability to solve problems will improve if he studies theory at the i-th day
# pi = how much it will improve if h epratcies a lot at the i-th day
# everyday, either theory or practice
# at least one of these days should be theoretical, and at least one should be practical
with open('input.txt', 'r') as inputfile:
    n = int(inputfile.readline())
    t = [int(x) for x in inputfile.readline().split(' ')]
    p = [int(x) for x in inputfile.readline().split(' ')]

    total = 0
    min_diff = float('inf')
    status = 0

    for i in range(n):
        if t[i] > p[i]:
            status |= 1
        elif t[i] < p[i]:
            status |= 2
        total += max(t[i], p[i])
        min_diff = min(min_diff, abs(t[i] - p[i]))

if status != 3:
    total -= min_diff

with open('output.txt', 'w') as output:
   output.write(str(total))
   output.write('\n')
