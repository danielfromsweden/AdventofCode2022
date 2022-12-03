import string
Lines = open("D:\Personal-Git\AdventofCode2022\day3\input1.txt", 'r').read().splitlines()
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letter_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}
sum = 0

for line in Lines:
    line_len = len(line)
    first_compartment = line[:line_len//2]
    second_compartment = line[line_len//2:]
    intersect = list(set(first_compartment).intersection(set(second_compartment)))
    sum += letter_dict.get(intersect[0])

print("Sum of intersecting letters:", sum)