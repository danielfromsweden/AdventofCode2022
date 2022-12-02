file = open("input1.txt", 'r')
Lines = file.readlines()
print(Lines)
win = 6
tie = 3
loss = 0
total_points = 0

for line in Lines:
    current_points = 0
    hand_op = line[0]
    hand_me = line[2]
    if hand_me=='X': # rock/loss
        current_points += 1
        if hand_op == 'A': # rock
            current_points += tie
        if hand_op == 'B': # paper
            current_points += loss
        if hand_op == 'C': # scissor
            current_points += win
    if hand_me=='Y': # paper
        current_points += 2
        if hand_op == 'A': # rock
            current_points += win
        if hand_op == 'B': # paper
            current_points += tie
        if hand_op == 'C': # scissor
            current_points += loss
    if hand_me == 'Z':  # scissor
        current_points += 3
        if hand_op == 'A': # rock
            current_points += loss
        if hand_op == 'B': # paper
            current_points += win
        if hand_op == 'C': # scissor
            current_points += tie
    total_points += current_points

    #print(line[0])
    #print(line[2])
    #print("Points: ", current_points)
print(total_points)