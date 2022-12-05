# with open('input_test', 'r') as f:
#     data = f.read()

with open('input', 'r') as f:
    data = f.read()
crates_order, movements = data.split('\n\n')
print(crates_order)
list_ = [[] for _ in range(9)]
for line in crates_order.splitlines()[:-1]:
    if line[1].strip():
        list_[0].append(line[1])
        
    if line[5].strip():
        list_[1].append(line[5])
        
    if line[9].strip():
        list_[2].append(line[9])
        
    if line[13].strip():
        list_[3].append(line[13])

    if line[17].strip():
        list_[4].append(line[17])

    if line[21].strip():
        list_[5].append(line[21])
        
    if line[25].strip():
        list_[6].append(line[25])
        
    if line[29].strip():
        list_[7].append(line[29])
    
    if line[33].strip():
        list_[8].append(line[33])
    

for line in movements.splitlines():
    print(line)
    number_crates, move_from, move_to = [int(x) for x in line.split() if x.strip() and not x.isalpha()]
    for _ in range(number_crates):
        list_[move_to - 1] = [list_[move_from - 1][0]] + list_[move_to - 1]
        del list_[move_from - 1][0]
    

print(''.join(x[0] for x in list_))
