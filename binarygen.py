length = 3
binaryarray = []

for n in range(0, (2**(length))):
    n2 = str(format(n, '#0' + str(length+2) + 'b'))[2:]
    binaryarray.append(str(n2))

print (binaryarray)
