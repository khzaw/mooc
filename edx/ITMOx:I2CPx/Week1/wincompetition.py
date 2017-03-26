with open('input.txt', 'r') as inputfile:
    N = int(inputfile.readline())
    result, i, L, T = 0, 0, 300 * 60, [int(i) for i in inputfile.readline().split(' ')]

T = sorted(T)
while i < N and L - T[i] >= 0:
    result, L, i = result + 1, L - T[i], i + 1

with open('output.txt', 'w') as output:
    output.write(str(result))
    output.write('\n')

