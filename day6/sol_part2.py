with open('input_test', 'r') as f:
    data = f.read()

with open('input', 'r') as f:
    data = f.read()
line = data.splitlines()[0]
print(line)
seen = []

words = 0
want = (0, 0)
for x in range(len(line) - 14):
    substr = line[x:x+14]
    if len(set(substr)) == 14:
        print(substr, x+14)
        break
