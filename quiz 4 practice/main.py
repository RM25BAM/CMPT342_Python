students = { 101 : 'Julia', 102 : 'Paul', 103 : 'Leela'}
if 101 in students:
    print(students[101])
else:
    None

del students[101]
print(len(students))

