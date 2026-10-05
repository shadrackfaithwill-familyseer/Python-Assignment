# students
student1 = {
    "name": "Pst.Familyseer",
    "phone": "0722545878",
    "age": 18,
    "location": "Nairobi",
    "dob": "2004-01-12"
}

student2 = {
    "name": "Festus",
    "phone": "0725441578",
    "age": 10,
    "location": "Mombasa",
    "dob": "2005-07-22"
}

student3 = {
    "name": "John",
    "phone": "07528874",
    "age": 19,
    "location": "Kisumu",
    "dob": "2006-11-08"
}

print("AllStudents:")
print(student1)
print(student2)
print(student3)

# put them in one dictionary so as to make it easy
students = {
    "s1": student1,
    "s2": student2,
    "s3": student3
}

# add a new student
students["s4"] = {
    "name": "Besti",
    "phone": "0745678901",
    "age": 17,
    "location": "Nakuru",
    "dob": "2008-01-30"
}

print("\nAfter adding Eve:")
print(students)
