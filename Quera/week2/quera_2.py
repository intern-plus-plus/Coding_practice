v = int(input())
if v==1:
	print(6)
	exit(0)
def surface(i,j,k):
	return (i*j*2)+(i*k*2)+(j*k*2)

minSurface = 100_000_000
scope = list(filter(lambda n: v%n==0, range(1,v)))
for i in scope:
	for j in scope:
		k = v/(i*j)
		if int(k)==k:
			if (i*j*k) == v:
				s = surface(i,j,k)
				if s < minSurface:
					minSurface = int(s)
print(minSurface)