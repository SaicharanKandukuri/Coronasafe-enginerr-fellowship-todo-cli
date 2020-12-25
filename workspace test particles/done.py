with open('done.txt', 'r') as f:
    for i, line in reversed(list(enumerate(f, start=1))):
        print('[{}] {}'.format(i, line.strip()))

a_file = open("done.txt", "r")

lines = a_file.readlines()
a_file.close()

print(lines)
print(len(lines))
del lines[1]

new_file = open("done.txt", "w+")

for line in lines:
    new_file.write(line)

new_file.close()

with open('done.txt', 'r') as f:
    for i, line in enumerate(f, start=1):
        print('[{}] {}'.format(i, line.strip()))