
eee = "hello " + "there"
eee = eee + 1
print(eee)

print(float(99) + 100)

i = 42
f = float(i)
print(f)
type(f)

print(10 / 2)
print(99 / 100)

sval = '123'
type(sval)
ival = int(sval)
type(ival)
print(ival + 1)

nsv = 'hello 1'
niv = int(nsv)
print(niv)

# input function resolves to a (str).
nam = input('How old are you?')
print("You are", nam)

# Need to use either float() or int() to convert
a = input('Input a number to multiply:')
b = input('Input the second number:')
a = int(a)
b = float(b)
print(a * b)

# Comments - What are they used for?

# Describe what is going to happen in the swquence of code
# Document who wrote the code or other ancillary information
# Turn off a line of code = perhaps temporarily

help(dict)

inp = input('What floor do you want to convert?')
usf = int(inp) + 1
print(usf)

name = input("Enter your name:")
print("Hello",name)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = int(hrs)
rate = float(rate)
print("Pay:",hrs * rate)
