
f = open('myData','r')

print(f)

print(f.read())

# print(f.readline(),end='')

# print(f.readline(),end='')

f1 = open('create_file','w')
print(f1.write('This is a new file created by python\n'))

f2 = open('append_file','a')
print(f1.write('This is a new file created by python\n'))
