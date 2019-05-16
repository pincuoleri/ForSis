
class A:
	a = 1
	def __init__(self):
		a += 1


	def test(self,b):
		return A.a


if __name__=='__main__':
	A().test('test-method')
	A.test('test-method')
	A.test('test-method')