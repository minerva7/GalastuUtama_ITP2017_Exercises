def gen(z):
    i = -1
    while z > i:
        yield z
        z -= 1

cd = gen(int(input('Insert number here: ')))
for z in cd:
    print(z)
print(type(cd))
