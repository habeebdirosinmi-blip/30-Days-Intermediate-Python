empty_list = []  
# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'mango', 'date', 'lime']
print(len(fruits))
first_item = fruits[0]
middle_item = fruits[len(fruits) // 2]
last_item = fruits[-1]
print(first_item, middle_item, last_item)  
mixed_data_types = ['Habeeb', 17, 1.60, 'Single', '116 Ademola street, Lagos']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])
it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Tesla')
it_companies.insert(len(it_companies) // 2, 'Netflix')
it_companies[3] = it_companies[3].upper()
joined_companies = '#;  '.join(it_companies)
print(joined_companies)
print('IBM' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_three = it_companies[:3]
last_three = it_companies[-3:]
mid = len(it_companies) // 2
middle_companies = it_companies[mid:mid+1] if len(it_companies) % 2 != 0 else it_companies[mid-1:mid+1]
it_companies.pop(0)
del it_companies[len(it_companies) // 2]
it_companies.pop()
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack_copy = full_stack.copy()
redux_index = full_stack_copy.index('Redux')
full_stack_copy.insert(redux_index + 1, 'Python')
full_stack_copy.insert(redux_index + 2, 'SQL')
print(full_stack_copy)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted: {ages}, Min: {min_age}, Max: {max_age}")
ages.extend([min_age, max_age])
ages.sort()
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]
print(f"Median Age: {median_age}")
average_age = sum(ages) / len(ages)
print(f"Average Age: {average_age}")
age_range = max_age - min_age
print(f"Age Range: {age_range}")
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print(f"|Min - Average|: {diff_min}, |Max - Average|: {diff_max}")
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
if len(countries) % 2 != 0:
    middle_countries = [countries[mid]]
else:
    middle_countries = countries[mid-1:mid+1]
print(f"Middle country: {middle_countries}")
half = (len(countries) + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(f"First Half: {first_half}")
print(f"Second Half: {second_half}")
c1, c2, c3, *scandic = countries
print(c1, c2, c3)
print(scandic)