with open('input/day1') as f:
	lines = f.read().splitlines()
	
from itertools import groupby

totals = list(reversed(sorted(sum(map(int, group)) for isgroup, group in groupby(lines, key=''.__eq__) if not isgroup)))
most_calories = totals[0]
sum_of_top_3 = sum(totals[0:3])

print(most_calories)
print(sum_of_top_3)

