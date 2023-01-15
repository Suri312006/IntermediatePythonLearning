example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])
#output

# 0 left
# 1 right
# 2 up
# 3 down

# correct method
for i, j in enumerate(example):
    print(i,j)

    # 0 left
    # 1 right
    # 2 up
    # 3 down

new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]