with open('input/day4') as f:
	lines = f.read().splitlines()
	
# Part 1
results = []
for line in lines:
	spans = [x.split('-') for x in line.split(',')]
	spans = [set(range(int(span[0]), int(span[1]) + 1)) for span in spans]
	results.append(spans[0].issubset(spans[1]) or spans[1].issubset(spans[0]))
total = sum(map(int,results))
print(total)

# Part 2
results = []
for line in lines:
	spans = [x.split('-') for x in line.split(',')]
	spans = [set(range(int(span[0]), int(span[1]) + 1)) for span in spans]
	results.append(len(spans[0].intersection(spans[1])) > 0)
total = sum(map(int,results))
print(total)

		