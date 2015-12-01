# import prettytable
from operator import xor
import sys

string1 = input("Enter the first gene/allele string: ")
string2 = input("Enter the second gene/allele string: ")


def check_valid(genes=[string1, string2]):
    '''Checks to see if an allele string is in a valid format'''
    valid = True
    wrongallele = []
    for y in genes:
        for x in range(1, (int((len(genes[0]) + len(genes[1]))/2) - 1)):
            if not xor(y[x].upper() == y[x-1].upper(),
                       y[x].upper() == y[x+1].upper()):
                valid = False
                if y not in wrongallele:
                    wrongallele.append(y)

    if wrongallele:
        return valid, wrongallele
    else:
        return valid, False

if len(string1) != len(string2):
    print ("Error: Allele string lengths different.")
    sys.exit()
elif not check_valid():
    x, y = check_valid()
    print ("Error: Allele string(s)", y, "not valid.")
    sys.exit()

gamete_array1 = []
possibilities_array1 = []
alleles_array1 = []

gamete_array2 = []
possibilities_array2 = []
alleles_array2 = []

string_length = int(len(string1))

# for x in string1:
#     if x.upper() not in alleles_array1:
#         alleles_array1.append(x.upper())
# for x in string2:
#     if x.upper() not in alleles_array2:
#         alleles_array2.append(x.upper())
#
#
# if alleles_array1 != alleles_array2:
#     print ("Error: Alleles in each string differ.")
#     sys.exit()

for x in range(0, string_length, 2):
    possibilities_array1.append([string1[x], string1[x+1]])
    possibilities_array2.append([string2[x], string2[x+1]])

print (possibilities_array1, possibilities_array2)

for x in range(0, len(possibilities_array1)):
    possibilities_array1[x] = sorted(possibilities_array1[x])

for x in range(0, len(possibilities_array2)):
    possibilities_array2[x] = sorted(possibilities_array2[x])

print (possibilities_array1, possibilities_array2)


temp = ""
for n in range(0, 2**(string_length//2-1)):
    n2 = str(format(n, '#0' + str(string_length+2) + 'b'))[2:]
    for a in possibilities_array1:
        for b in n2:
            temp += a[int(b)]
    temp += ","

print (temp)
