x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

# for a,b,c in zip(x,y,z):
#     print(a,b)
#[print(a,b,c) for a,b,c in zip(x,y,z)]
print(zip(x,y,z))

for i in zip(x,y,z):
    print(i)