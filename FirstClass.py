#simple function to check if an element is a number
def isNumber(i):
	try:
		float(i)
		return True
	except ValueError:
		return False

def sum_gen(x):
	if type(x) == list:
		def sum_list(value):
			sum_of_elem = 0
			for i in value:
				if isNumber(i):
					sum_of_elem += i
			return sum_of_elem
		return sum_list
	elif type(x) == dict:
		def sum_dict(value):
			sum_of_elem = 0
			for i in value.values():
				if isNumber(i):
					sum_of_elem += i
			for j in value.keys():
				if isNumber(j):
					sum_of_elem += j
			return sum_of_elem
		return sum_dict
	elif type(x) == float or type(x) == int:
		def sum_other(value):
			a = "You cannot sum this value!"
			return a
		return sum_other
	elif type(x) == tuple:
		def sum_tuple(value):
			sum_of_elem = 0
			for i in value:
				if isNumber(i):
					sum_of_elem += i
			return sum_of_elem
		return sum_tuple

sumlist = sum_gen([])

sumdict = sum_gen({})

sumtuple = sum_gen(())

sumint = sum_gen(12)

sumfloat = sum_gen(12.5)

sl = sumlist([1,2,3.2, 'w'])
print sl

dl = sumdict({1:'a',2:3,'x':12.6})
print dl

st = sumtuple((1,2,"foo",6))
print st

si = sumint(12)
print si

sf = sumfloat(12.5)
print sf
