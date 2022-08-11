file = 'data.bin'


s = "Hello Python"
x = 420
y = 12.0


with open("file", "w") as new_file:
    new_file.write(s+'\n')
    new_file.write(str(x)+'\n')
    new_file.write(str(y))


with open("file", "rb") as new_file:
    data = new_file.read().splitlines()
    print(data[0])
    print(data[1])
    print(data[2])

for line in data:
    print(line)

print(data)
