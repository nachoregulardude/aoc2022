with open('input', 'r') as f:
    data = f.read()

elf_cals = [
    sum(int(cal) for cal in elf.split('\n') if cal.strip())
    for elf in data.split('\n\n')
        ]
part_1 = max(elf_cals)
        
part_2 = sum(
        sorted(elf_cals, reverse=True)[:3]
        )

max_3 = []
for _ in range(3):
    max_ = max(elf_cals)
    elf_cals.pop(elf_cals.index(max_))
    max_3.append(max_)
# part_2 = sum(max_3)

print(f"{part_1=}")
print(f"{part_2=}")
