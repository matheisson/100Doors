doors = [0] * 100

for y in range(1,101):
	for x in range(0,100):
		if (x+1)%y == 0:
			if doors[x] == 0:
				doors[x] = 1
			else:
				doors[x] = 0
for x in range(0,100):
	if doors[x] == 1:
		print(x+1)
