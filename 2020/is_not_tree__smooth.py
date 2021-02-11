class __(int):
	def __new__(cls, num):
		i = super().__new__(cls, num)
		i._2 = None
		i._3 = None
		return i
 
def p(b, m, a=[__(1)]):
	while True:
		n = a.pop(0)
		if n>m: break
		if n not in b: b.append(n)
		n._2 = __(2*n)
		n._3 = __(3*n)
		a.insert(0, n._2)
		a.insert(0, n._3)
		a.sort()
 
b = []
p(b, 3000)
print(b)
 
def pp(arr, m, b=[1]):
	while True:
		n = b.pop(0)
		if n>m: break
		if n not in arr: arr.append(n)
		b.insert(0, 2*n)
		b.insert(0, 3*n)
		b.sort()
 
c = []
pp(c, 3000)
print(c)
