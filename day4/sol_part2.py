# with open('input_test', 'r') as f:
#     data = f.read()

with open('input', 'r') as f:
    data = f.read()
lines = data.splitlines()
count = 0
for line in lines:
    first_elf, second_elf = line.split(',')
    start_first_elf = int(first_elf.split('-')[0])
    end_first_elf = int(first_elf.split('-')[1])
    start_second_elf = int(second_elf.split('-')[0])
    end_second_elf = int(second_elf.split('-')[1])
    if end_first_elf < start_second_elf or end_second_elf < start_first_elf:
        continue
    count += 1
    
print(count)
