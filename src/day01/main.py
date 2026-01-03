path = './input_data.txt'
sequence = []  
start_position = 50
result1 = 0
result2 = 0

with open(path, 'r') as file:
    for line in file:
        sequence.append(line.strip())

def dial(pos, move):
    direction = move[0]
    steps = int(move[1:])
    inc = 0
    while steps > 0:
        if direction == 'L':
            pos -= 1
            if pos == -1:
                pos = 99
        if direction == 'R':
            pos += 1
            if pos == 100:
                pos = 0
        steps -= 1
        if pos == 0:
            inc += 1
    return pos, inc

for move in sequence:
    end_position, inc = dial(start_position, move)
    if end_position == 0:
        result1 += 1
    result2 += inc
    start_position = end_position

print('The password for part 1 is: ' + str(result1))
print('The password for part 2 is: ' + str(result2))