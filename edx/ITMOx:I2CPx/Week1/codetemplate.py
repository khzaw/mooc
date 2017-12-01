with open('input.txt', 'r') as input_file:
    W, H = [int(x) for x in input_file.readline().split(' ')]

    x_coord, y_coord = {}, {}
    
    for i in range(H):
        row = input_file.readline()
        for j in range(W):
            c = row[j]
            y_coord[c], x_coord[c], j = H-i, j+1, j+1

    L = 0
    language = []
    distance= [0 for _ in range(3)]
    # assert input_file.readline() in ['\n', '\r\n']

    while L < 3:
        language += input_file.readline(),
        input_file.readline()
        nextline, last = input_file.readline().strip(), None
        while nextline not in ['%TEMPLATE-START%\n', '%TEMPLATE-START%\r\n', '%TEMPLATE_END%\n', '%TEMPLATE_END%\r\n']:
            if last:
                distance[L] += max(abs(y_coord[nextline[0]] - y_coord[last]), 
                                   abs(x_coord[nextline[0]] - x_coord[last]))
            for i in range(len(nextline) - 2):
                c1, c2 = nextline[i], nextline[i+1]
                distance[L] += max(abs(y_coord[c2] - y_coord[c1]),
                                   abs(x_coord[c2] - x_coord[c1]))

            last = nextline[-2]
            nextline = input_file.readline()
        L += 1

with open('output.txt', 'w') as output:
    output.write(str(language[distance.index(min(distance))]))
    output.write(str(min(distance)))
    output.write('\n')
