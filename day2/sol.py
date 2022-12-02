# with open('input_test', 'r') as f:
#     data = f.read()

with open('input', 'r') as f:
    data = f.read()

mapping_dict = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissor',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissor'
        }

beats = {
        'rock': 'scissor',
        'scissor': 'paper',
        'paper': 'rock'
        }
beats_rev = {v: k for k, v in beats.items()}
extra_point = {'rock': 1, 'paper': 2, 'scissor': 3}
for k, v in mapping_dict.items():
    if k not in ('X', 'Y', 'Z'): # for part 2
        data = data.replace(k, v)
    
    
n = 0
for line in data.splitlines():
    opponent_choice, our_choice =  line.split()
    if our_choice == 'X' :
    # or our_choice == opponent_choice:
        n += extra_point[beats[opponent_choice]]
    elif our_choice == 'Y' :
    # or beats[opponent_choice] != our_choice:
        n += extra_point[opponent_choice] + 3
    else:
        n += extra_point[beats_rev[opponent_choice]] + 6
    # n += extra_point[beats_rev[opponent_choice]]

    
print(n)
