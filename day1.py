print('Day 1:')
input_file = open("input.txt", "r")
input = input_file.read()
data_list = input.split("\n")
elf_sum = 0
max_sum = 0
for elf_calories in data_list:
    data_list_calories = elf_calories.split(" ")
    if data_list_calories[0] != "":
        elf_sum += int(data_list_calories[0])
    else:
        if elf_sum > max_sum:
            max_sum = elf_sum
        elf_sum = 0
print("Max sum is", max_sum)
