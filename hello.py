#this is a file for reference in the future when i forget 

print('hello world')
i = 21
print(f"i is {i}")

if x < 0:
    print('x is blah')
elif x > 0:
    print('x is elif')
else:
    print('x is nah')

name = 'alive'
coordinates = (10,2,3,5,7)
name = ['alice', 'barbara', 'ugly']

s = set()
s.add(1)
s.add(21)
s.add(13)
s.add(11)
s.add(7)


def square(x):
    return x * x

for i in range(122):
    print("{} squared is {}".format(i, square(i)))
