# lists are faster but uses memory
xyz = [i for i in range(50000000)]

print(xyz)

# abc = []
# for i in range(500000):
#     abc.append(i)
#
# print(abc)

# # generators are slower but dont use as much memory
lmao = (i for i in range(50000000))
print(lmao)
#
# for i in lmao:
#     print(i)