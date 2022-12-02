file = open("input1.txt", 'r')
Lines = file.readlines()
#print(Lines)
win = 6
tie = 3
loss = 0
r = 1
p = 2
s = 3

total_points = 0

for line in Lines:
    current_points = 0
    hand_op = line[0]
    hand_me = line[2]
    if hand_me=='X': # loss
        current_points += 0
        if hand_op == 'A': #
            current_points += s
        if hand_op == 'B': #
            current_points += r
        if hand_op == 'C': #
            current_points += p
    if hand_me=='Y': # tie
        current_points += 3
        if hand_op == 'A': # rock
            current_points += r
        if hand_op == 'B': # paper
            current_points += p
        if hand_op == 'C': # scissor
            current_points += s
    if hand_me == 'Z':  # win
        current_points += 6
        if hand_op == 'A': # rock
            current_points += p
        if hand_op == 'B': # paper
            current_points += s
        if hand_op == 'C': # scissor
            current_points += r
    total_points += current_points

    #print(line[0])
    #print(line[2])
    #print("Points: ", current_points)
print(total_points)