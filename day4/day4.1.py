import string
Lines = open("D:\Personal-Git\AdventofCode2022\day4\input.txt", 'r').read().splitlines()
count = 0

for line in Lines:
    line = line.split(',')
    numbers = [(line[0]).split('-'), (line[1]).split('-')]
    first_list = list(range(int(numbers[0][0]), int(numbers[0][1])+1))
    second_list = list(range(int(numbers[1][0]), int(numbers[1][1])+1))
    list = [elem for elem in numbers]
    result_1_to_2 = all(elem in first_list  for elem in second_list)
    result_2_to_1 = all(elem in second_list  for elem in first_list)
    if result_1_to_2 or result_2_to_1:
        count += 1
print("The number of fully contained pairs are:", count)