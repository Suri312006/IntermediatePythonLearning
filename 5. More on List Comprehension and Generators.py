input_list = [5, 12, 35, 105, 200, 14, 25, 10000]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


# generator
xyz = (i for i in input_list if div_by_five(i))

# #logic of thingy above
# xyz=[]
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)

# [print(i) for i in xyz]


# list
xyz = [i for i in input_list if div_by_five(i)]
# [print(i) for i in xyz]


abc = (((i, ii) for ii in range(5)) for i in range(5))

# for i in range(5):
#     for ii in range(5):
#         print(i,ii)

for i in abc:
    for ii in i:
        print(ii)
