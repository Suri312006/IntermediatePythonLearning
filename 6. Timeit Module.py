import timeit

# print(timeit.timeit("1+3", number= 6000000))

# input_list = range(100)
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# xyz = (i for i in input_list if div_by_five(i))
#
# abc = [i for i in input_list if div_by_five(i)]
#
# for i in xyz:
#     print(i)
#
# print(abc)


# cosider timeit as a seperate script, needs its own imports and defenitions and stuff
print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    x = i
''', number=500000))
