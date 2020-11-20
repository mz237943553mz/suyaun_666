#coding=utf-8

class A():

	def test_a(self):
		print("====a======")

class B():
	def test_a(self):
		print("====b======")

# 就近原则
class C(B,A):

	def test_a(self):
		print("====c=====")
#
# c=C()
# c.test_a()
# c.test_b()

c=C()
c.test_a()

