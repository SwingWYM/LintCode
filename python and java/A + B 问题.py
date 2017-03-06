a = 9
b = 8
def add(a,b):
	print('b:',b)
	if b == 0:
		return a
	if a == 0:
		return b
	if a == -b:
		return 0
	c = a ^ b
	d = (a & b) << 1
	return add(c,d)
s = add(a,b)
print(s)
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
