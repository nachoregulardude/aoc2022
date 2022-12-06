with open('input_test', 'r') as f:
    data = f.read()

with open('input', 'r') as f:
    data = f.read()
line = data.splitlines()[-1]
seen = []

words = 0
for x in line:
    words += 1
    if x not in seen:
        seen.append(x)
        if len(seen) == 4:
            want = seen, words
            break
    else:
        seen = []
print(want[0], want[1] - 1)
    
    
