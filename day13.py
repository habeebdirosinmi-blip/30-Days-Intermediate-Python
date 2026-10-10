numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print("Filtered numbers:", filtered_numbers)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print("Flattened list:", flattened_list)
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples:")
for t in list_of_tuples:
    print(t)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print("Formatted countries list:", formatted_countries)
countries_dict = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print("Countries as dictionaries:", countries_dict)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print("Concatenated names:", concatenated_names)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x, y, m: y - (m * x)
print("Slope (for points (1, 2) and (3, 6)):", slope(1, 2, 3, 6))
print("Y-intercept (for point (1, 2) with slope 2.0):", y_intercept(1, 2, 2.0))