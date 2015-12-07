from prettytable import PrettyTable
from operator import xor
import sys

# string1 = input("Enter the first gene/allele string: ")
# string2 = input("Enter the second gene/allele string: ")

string1 = "AaLlgg"
string2 = "AaLlgg"


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

for x in range(0, len(possibilities_array1)):
    possibilities_array1[x] = sorted(possibilities_array1[x])

for x in range(0, len(possibilities_array2)):
    possibilities_array2[x] = sorted(possibilities_array2[x])

# print (possibilities_array1)
# print (possibilities_array2)


# temp = ""
# for n in range(0, 2**(string_length//2-1)):
#     n2 = str(format(n, '#0' + str(string_length+2) + 'b'))[2:]
#     for a in possibilities_array1:
#         for b in n2:
#             temp += a[int(b)]
#     temp += ","

binaryarray = []

for n in range(0, (2**(string_length//2))):
    n2 = str(format(n, '#0' + str((string_length//2)+2) + 'b'))[2:]
    binaryarray.append(str(n2))


temp1, temp2 = "", ""
for x in binaryarray:
    for y in range(0, len(possibilities_array1)):
        temp1 += possibilities_array1[y][int(str(x)[y])]
        temp2 += possibilities_array2[y][int(str(x)[y])]

    gamete_array1.append(temp1)
    gamete_array2.append(temp2)
    temp1, temp2 = "", ""

zygote_array = []
for x in range(0, len(binaryarray)):
    zygote_array.append([])

temp = ""


def gamete_combine(g1, g2):
    zygote = []
    zygote = ""
    for x in range(0, len(g1)):
        zygote += ''.join(sorted(g1[x] + g2[x]))
    return zygote


for x in range(0, len(gamete_array1)):
    for y in range(0, len(gamete_array2)):
        # zygote_array[x].append(sorted(gamete_array1[x] + gamete_array2[y]))
        zygote_array[x].append(
            gamete_combine(gamete_array1[x], gamete_array2[y]))
        temp = ''

# for x in zygote_array:
#     print (x)


# def table_draw(gamete_array1, gamete_array2, zygote_array):
#     width = 1 + len(gamete_array1[0]) + 1 + (len(zygote_array) *
#                                              (len(zygote_array[0]) + 2)) + 1
#     sys.stdout.write('┌')
#     for x in range(0, width):
#         sys.stdout.write('—')
#     sys.stdout.write('┐')
# print ('\n')
# table_draw(gamete_array1, gamete_array2, zygote_array)
print (gamete_array1)
print (gamete_array2)
square = PrettyTable()
square.padding_width = 1
print ("ayylmao")
temp = []
square.add_row(["Gametes"] + gamete_array1)
for x in range(0, len(gamete_array1)+1):
    temp.append([""])
square.add_row(temp)
temp = []
for x in range(0, len(gamete_array1)):
    # for y in zygote_array[x]:
    #     temp.append(y)
    temp = gamete_array1[x].split()
    for z in zygote_array[x]:
        temp.append(z)
    square.add_row(temp)

# square.add_row()
print ('\n')
print (square)



