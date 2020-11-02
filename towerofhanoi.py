def hanoi(n, s, a, t):
	print('#%s Hanoi: %s %s %s' % (n, s, a, t))
	if n > 0:
		hanoi(n-1, s, t, a)
		if s[0]:
			disk = s[0].pop()
			print('Move %s to %s' % (str(disk), t[1]))
			t[0].append(disk)
			hanoi(n-1, a, s, t)

hSource = ([0, 1, 2], 'Source')
hAux = ([], 'Auxiliary')
hTarget = ([], 'Target')

hanoi(len(hSource[0]), hSource, hAux, hTarget)
print('\n%s\n%s\n%s' % (hSource[0], hAux[0], hTarget[0]))