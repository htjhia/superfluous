def permutation(n, k):
	"""
	Source: https://stackoverflow.com/a/2837693/14185713
	"""
	for i in range(len(n)):
		if k == 1:
			yield (n[0], )
		else:
			for j in permutation(n[i+1:], k-1):
				yield (n[i], ) + j

for i in permutation([1, 2, 3, 4], 3):
	print(i)