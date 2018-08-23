# we have 1,2,3,4, compute how many conbiantions with three unrepeated word
tem = []
count = 0
for x in range(1,5):
	for y in range(1,5):
		for z in range(1,5):
			if x != y and x!= z and y != z:
				tem.append(x*100+y*10+z)
				count += 1
print("There are {} combinations: {}".format(count,tem))
