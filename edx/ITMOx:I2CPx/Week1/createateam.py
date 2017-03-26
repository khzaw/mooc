import itertools

with open('createateam.in', 'rb') as input_file:
    A = list(map(int, input_file.readline().decode('utf-8').split(' ')))
    B = list(map(int, input_file.readline().decode('utf-8').split(' ')))
    C = list(map(int, input_file.readline().decode('utf-8').split(' ')))

    # fuck it, brute force FTW!
    answer = 0
    for i, j, k in itertools.permutations(range(3)):
        answer = max(answer, A[i]*A[i] + B[j]*B[j] + C[k]*C[k])

with open('createateam.out', 'wb') as output:
    output.write(str(answer ** 0.5).encode('utf-8'))
    output.write('\n'.encode('utf-8'))
