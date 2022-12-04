with open('input/day3') as f:
	lines = f.read().splitlines()
	
def priority(item):
	if ord(item) <= ord('Z') :
		return ord(item) - ord('A') + 1 + 26
	else:
		return ord(item) - ord('a') + 1
	
# Part 1
total = sum(priority((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()) for line in lines)
print(total)

# Part 2
total = sum(priority(set.intersection(*(set(x) for x in lines[l:(l+3)])).pop()) for l in range(0, len(lines), 3))
print(total)