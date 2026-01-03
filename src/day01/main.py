path = './input_data.txt'
sequence = []  
start_position = 50
password = 0

with open(path, 'r') as file:
    for line in file:
        sequence.append(line.strip())

def dial(pos, move):
    direction = move[0]
    steps = int(move[1:])
    #print(pos, move, direction, steps)
    while steps > 0:
        if direction == 'L':
            pos = pos -1
            if pos == -1:
                pos = 99
        if direction == 'R':
            pos = pos + 1
            if pos == 100:
                pos = 0
        steps = steps - 1
        #print (pos, direction, steps)
    return(pos)




for move in sequence:
    end_position = dial(start_position, move)
    if end_position == 0:
        password = password + 1
    start_position = end_position
    #print('Final position: ' + str(end_position))

print('The password is: ' + str(password))