# ti = how much ability to solve problems will improve if he studies theory at the i-th day
# pi = how much it will improve if h epratcies a lot at the i-th day
# everyday, either theory or practice
# at least one of these days should be theoretical, and at least one should be practical

with open('input.txt', 'rb') as input_file:
    n = int(input_file.readline())
    t = list(map(int, input_file.readline().decode('utf-8').split(' ')))
    p = list(map(int, input_file.readline().decode('utf-8').split(' ')))
    total_t = 0
    total_p = 0
    total = 0
    for i in range(n):
        if(p[i] > t[i]):
            total = total + p[i]
            total_p = total_p + 1
        else:
            total = total + t[i]
            total_t = total_t + 1
    print(total, total_t, total_p)
# with open('output.txt', 'wb') as output_file:
#     output_file.write(str(total).encode('utf-8'))
#     output_file.write('\n'.encode('utf-8'))
