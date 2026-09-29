'day 2 : 30 Days of python programming'
first_name = 'muhammad'
last_name = 'kanu'
full_name = first_name + ' ' + last_name
country = 'Nigeria'
city = 'Lagos'
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True
brand, model, year_built = 'samsung', 'A23', 2023
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
first_name_len = len(first_name)
print('First name length:', first_name_len)
last_name_len = len(last_name)
print('Is first name longer than last name?', first_name_len > last_name_len)
num_one = 5
num_two = 4
total = num_one + num_two
print('Total:', total)
diff = num_one - num_two
print('Difference:', diff)
product = num_two * num_one
print('Product:', product)
division = num_one / num_two
print('Division:', division)
remainder = num_two % num_one
print('Remainder:', remainder)
exp = num_one ** num_two
print('Exponentiation:', exp)
floor_division = num_one // num_two
print('Floor division:', floor_division)
import math
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
first_name_len = len(first_name)
print('First name length:', first_name_len)
last_name_len = len(last_name)
print('Is first name longer than last name?', first_name_len > last_name_len)
num_one = 5
num_two = 4
total = num_one + num_two
print('Total:', total)
diff = num_one - num_two
print('Difference:', diff)
product = num_two * num_one
print('Product:', product)
division = num_one / num_two
print('Division:', division)
remainder = num_two % num_one
print('Remainder:', remainder)
exp = num_one ** num_two
print('Exponentiation:', exp)
floor_division = num_one // num_two
print('Floor division:', floor_division)
radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
print('Area of circle:', area_of_circle)
print('Circumference of circle:', circum_of_circle)
user_radius = float(input('Enter radius of circle: '))
user_area = math.pi * (user_radius ** 2)
print('Area with user radius:', user_area)
user_first_name = input('Enter your first name: ')
user_last_name = input('Enter your last name: ')
user_country = input('Enter your country: ')
user_age = int(input('Enter your age: '))
help('keywords')