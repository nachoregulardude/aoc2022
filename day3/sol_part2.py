from string import ascii_letters
# with open('input_test', 'r') as f:
#     data = f.read()

with open('input', 'r') as f:
    data = f.read()

priority_dict = {
        letter: priority
        for priority, letter in enumerate(ascii_letters, 1)
        }
group_priority = []
lines = data.splitlines()
for idx in range(0, len(lines) - 2, 3):
    group = lines[idx: idx + 3]
    for letter in group[0]:
        if all(letter in group[x] for x in  range(1, 3)):
            group_priority.append(priority_dict[letter])
            break
    
print(sum(group_priority))
