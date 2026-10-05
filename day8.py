dog = {}
dog['name'] = 'Jack'
dog['color'] = 'White'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 1
student = {
    'first_name': 'Habeeb',
    'last_name': 'Durosinmi',
    'gender': 'Male',
    'age': 16,
    'marital_status': 'Single',
    'skills': ['Python', 'SQL'],
    'country': 'Nigeria',
    'city': 'Lagos',
    'address': '116 Oniru Estate'
}
student_length = len(student)
print("Student dict length:", student_length)
skills = student['skills']
print("Skills:", skills)
print("Skills data type:", type(skills))  
student['skills'].extend(['Excel', 'Power BI'])
keys_list = list(student.keys())
print("Keys:", keys_list)
values_list = list(student.values())
print("Values:", values_list)
student_tuples = list(student.items())
print("Tuples:", student_tuples)
del student['marital_status']
del dog
