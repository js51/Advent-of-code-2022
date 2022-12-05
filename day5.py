with open('input/day5') as f:
	lines = f.read().splitlines()

part_1 = False

stacks = []
for l, line in enumerate(lines):
	if '1' in line:
		instructions_index = l + 2
		break
	stack = []
	for i in range(0, len(line), 4):
		stack.append("".join(line[i:i+4]).strip(' ').strip(']').strip('['))
	stacks.append(stack)

stacks = list(list("".join(stack).strip(' ')) for stack in map(list, zip(*stacks)))

for line in lines[instructions_index:]:
	instruction = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
	m, f, t = tuple(int(x) for x in instruction)
	if part_1:
		for _ in range(m):
			item = stacks[f-1].pop(0)
			stacks[t-1] = [item] + stacks[t-1]
	else: # Part 2
		items = [stacks[f-1].pop(0) for _ in range(m)]
		stacks[t-1] = items + stacks[t-1]
	
message = "".join(stack[0] for stack in stacks)
print(message)

	