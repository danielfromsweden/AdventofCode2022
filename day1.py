print('Day 1:')
input_file = open("input.txt", "r")
data = input_file.read()
data_list = data.split("\n")
elf_sum = 0
max_sum = 0
elf_list = []
#print(data_list)
count = 0
#print(len(data_list))
for elf_calories in data_list:
    count += 1
    #print(count)
    #print(elf_calories)
    if elf_calories != '':
        elf_calories = int(elf_calories)
        elf_sum += elf_calories
    else:
        elf_list.append(elf_sum)
        elf_sum = 0
    if(count == len(data_list)):
        elf_list.append((elf_sum))
elf_list.sort(reverse=True)
#print(elf_list)
print("Max sum is", elf_list[0])
print("The top 3 calories are", elf_list[0:3] )
print("The total of top 3 is: ", elf_list[0]+elf_list[1]+elf_list[2])
