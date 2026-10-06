age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    missing_years = 18 - age
    print(f"You need {missing_years} more {'year' if missing_years == 1 else 'years'} to learn to drive.")

print()
my_age = 16
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} {'year' if diff == 1 else 'years'} older than me.")
elif my_age > your_age:
    diff = my_age - your_age
    print(f"I am {diff} {'year' if diff == 1 else 'years'} older than you.")
else:
    print("We are the same age!")

print()
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

print("\n" + "=" * 40 + "\n")
score = int(input("Enter score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score <= 59:
    print("Grade: F")
else:
    print("Invalid score entered.")

print()

month = input("Enter month: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered.")

print()
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").strip().lower()

if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)

print("\n" + "=" * 40 + "\n")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person and person['skills']:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

if 'skills' in person:
    user_skills = set(person['skills'])
    if user_skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(user_skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(user_skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")