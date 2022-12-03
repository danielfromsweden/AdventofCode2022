import string
Lines = open("D:\Personal-Git\AdventofCode2022\day3\input1.txt", 'r').read().splitlines()
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letter_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}
sum = 0

for i in range(0, len(Lines)-2, 3):
    intersect = list(set(Lines[i]) & set(Lines[i+1]) & set(Lines[i+2]))
    sum += letter_dict.get(intersect[0])

print("Sum of intersecting letters:", sum)