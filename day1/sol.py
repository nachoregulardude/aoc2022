with open('input', 'r') as f:
    data = f.read()


elf_cals = []
for elf in data.split('\n\n'):
    elf_cal = sum(int(cal) for cal in elf.split('\n') if cal.strip())
    elf_cals.append(elf_cal)
        
max_3 = []
for _ in range(3):
    max_ = max(elf_cals)
    elf_cals.pop(elf_cals.index(max_))
    max_3.append(max_)

print(sum(max_3))
