names = ['Surendra', 'Naila', 'Andres', 'Adrien']
#
# for name in names:
#
# print('Hello there, '+ name)
# print(' '.join(['Hello there,', name]))
#
# concatanating more than 2 strings, use join.
# print(', '.join(names))
#
# import os
#
# location_of_files = 'C:\\Users\\suri3\\PycharmProjects\\IntermediatePythonLearning'
# file_name = 'example.txt'
#
# with open(os.path.join(location_of_files, file_name)) as cock:
#     print(cock.read())


who = 'Suri'
how_many = 12

#Suri bought 12 cocks today!

#the wrong way to do string formatting
print(who, "bought", how_many, "cocks today!")

#the correct way to do string formatting
print('{} bought {} cocks today!'.format(who, how_many))
