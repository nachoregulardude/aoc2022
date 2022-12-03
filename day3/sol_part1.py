from string import ascii_letters
# with open('input_test', 'r') as f:
#     data = f.read()

with open('input', 'r') as f:
    data = f.read()

priority_dict = {
        letter: priority
        for priority, letter in enumerate(ascii_letters, 1)
        }
repeated_item_priority = []
for rucksack in data.splitlines():
    number_of_items = len(rucksack)
    comp1, comp2 = rucksack[:number_of_items//2], rucksack[number_of_items//2:]
    for item in comp1:
        if item in comp2: 
            repeated_item_priority.append(priority_dict[item])
            break
    
print(sum(repeated_item_priority))
