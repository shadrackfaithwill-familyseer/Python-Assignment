#Here is a list of students with age
students = [
    {"name": "John", "age": 19},
    {"name": "Ben", "age": 30},
    {"name": "James", "age": 19},
    {"name": "John", "age": 21}
]

print("Original list:")
print(students)

# add a student
students.append({"name": "Jose", "age": 18})
print("\nAfter adding Eve:")
print(students)

# edit Bob's age
students[1]["age"] = 31
print("\nAfter editing Ben's age:")
print(students)

# delete Jose
del students[2]
print("\nAfter deleting Charlie:")
print(students)
