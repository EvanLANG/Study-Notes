# an "complete" word is a word equeals its sum of all factor
# form 100 to 1000

from math import sqrt
tem = []
for i in range(1,10001):
	mean = int(sqrt(i)) + 1
	sum_ = 0
	for x in range(1, mean+1):
		if i%x == 0:
			sum_ += x
			#print(i,x)

	if i == sum_:
		tem.append(i)
		print("There are {} words: {}".format(len(tem),tem))
