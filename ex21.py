
def add(a, b):

	print("Adding {} and {}".format(a,b))

	return a+b

def subtract(a, b):

	print("subtract %d - %d" %(a, b))

	return a-b

def multiply(a, b):

	print("Multiply %d * %d" %(a, b))

	return a*b

def devide(a, b):

	print("Devide %d / %d " %(a,b))

	return a/b

print("Let's do some math with just functions!")

age = add(30 , 5)

height = subtract(78, 4)

weight = multiply(90, 2)

iq = devide(100 , 2)

print("age: %d , height: %d , weight: %d , iq: %d" %(age, height, weight ,iq))

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight,devide(iq,2))))

print("That becomes",what, "can you guess" )

