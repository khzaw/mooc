with open('input.txt', 'r') as input_file:
    sides = [int(x) for x in input_file.readline().split(' ')] 
    answer = sum(sides) / 6

with open('output.txt', 'w') as output:
    output.write(str(answer))
    output.write('\n')
