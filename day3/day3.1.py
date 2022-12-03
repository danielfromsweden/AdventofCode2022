import string
Lines = open("D:\Personal-Git\AdventofCode2022\day3\input1.txt", 'r').read().splitlines()
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
letter_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}
sum = 0

for line in Lines:
    sum += letter_dict.get(list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0])

print("Sum of intersecting letters:", sum)