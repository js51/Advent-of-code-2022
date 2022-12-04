with open('input/day2') as f:
	lines = f.read().splitlines()

# Part 1
D = {'A':0,'B':1,'C':2,'X':0,'Y':1,'Z':2,0:(3,0,6),1:(6,3,0),2:(0,6,3)}
score = sum([ D[game[-1]] + 1 + D[D[game[-1]]][D[game[0]]] for game in lines ])
print(score)

# Part 2
D = {'A':0,'B':1,'C':2,'X':0,'Y':3,'Z':6,0:(2,0,1),3:(0,1,2),6:(1,2,0)}
score = sum([ D[game[-1]] + D[D[game[-1]]][D[game[0]]] + 1 for game in lines ])
print(score)