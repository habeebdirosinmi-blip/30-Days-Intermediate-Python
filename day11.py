import math
import cmath
import keyword
from collections import Counter
def add_two_numbers(a, b):
    return a + b

print("add_two_numbers(3, 5):", add_two_numbers(3, 5))
def area_of_circle(r):
    return math.pi * r * r
print("area_of_circle(5):", area_of_circle(5))
def add_all_nums(*args):
    total = 0
    for item in args:
        if not isinstance(item, (int, float)):
            return f"Error: All arguments must be numbers. Found invalid item: {item} ({type(item).__name__})"
        total += item
    return total
print("add_all_nums(1, 2, 3, 4):", add_all_nums(1, 2, 3, 4))
print("add_all_nums(1, 'a', 3):", add_all_nums(1, 'a', 3))
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
print("convert_celsius_to_fahrenheit(25):", convert_celsius_to_fahrenheit(25))
def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'
print("check_season('October'):", check_season("October"))
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print("calculate_slope(1, 2, 3, 6):", calculate_slope(1, 2, 3, 6))
def solve_quadratic_eqn(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    x1 = sol1.real if sol1.imag == 0 else sol1
    x2 = sol2.real if sol2.imag == 0 else sol2
    return (x1, x2)
print("solve_quadratic_eqn(1, -3, 2):", solve_quadratic_eqn(1, -3, 2))
def print_list(lst):
    for item in lst:
        print("   item:", item)
print("print_list(['a', 'b', 'c']):")
print_list(['a', 'b', 'c'])
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print("reverse_list([1, 2, 3, 4, 5]):", reverse_list([1, 2, 3, 4, 5]))
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]
print("capitalize_list_items(['apple', 'banana']):", capitalize_list_items(["apple", "banana"]))
def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list
print("add_item(['apple', 'banana'], 'orange'):", add_item(['apple', 'banana'], 'orange'))
def remove_item(lst, item):
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list
print("remove_item(['apple', 'banana', 'orange'], 'banana'):", remove_item(['apple', 'banana', 'orange'], 'banana'))
def sum_of_numbers(n):
    return sum(range(1, n + 1))
print("sum_of_numbers(10):", sum_of_numbers(10))
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
print("sum_of_odds(10):", sum_of_odds(10))
def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print("sum_of_even(10):", sum_of_even(10))
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    print(f"   The number of odds are {odds}.")
    print(f"   The number of evens are {evens}.")
print("evens_and_odds(100):")
evens_and_odds(100)
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("factorial(5):", factorial(5))
def is_empty(val):
    return not bool(val)
print("is_empty([]):", is_empty([]))
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0
print("calculate_mean([1, 2, 3, 4, 5]):", calculate_mean([1, 2, 3, 4, 5]))
def calculate_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]
print("calculate_median([1, 3, 2, 5, 4]):", calculate_median([1, 3, 2, 5, 4]))
def calculate_mode(lst):
    if not lst:
        return None
    counts = Counter(lst)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]
print("calculate_mode([1, 2, 2, 3, 4]):", calculate_mode([1, 2, 2, 3, 4]))
def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0
print("calculate_range([1, 2, 3, 4, 10]):", calculate_range([1, 2, 3, 4, 10]))
def calculate_variance(lst):
    if not lst:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
print("calculate_variance([1, 2, 3, 4, 5]):", calculate_variance([1, 2, 3, 4, 5]))
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
print("calculate_std([1, 2, 3, 4, 5]):", calculate_std([1, 2, 3, 4, 5]))
def greet(name="Guest"):
    print(f"   Hello, {name}!")
print("greet() & greet('Alice'):")
greet()
greet("Alice")
def show_args(**kwargs):
    formatted_args = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
    print(f"   Received: {formatted_args}")
print("show_args(a=1, b=2):")
show_args(a=1, b=2)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("is_prime(17):", is_prime(17))
def are_all_unique(lst):
    return len(lst) == len(set(lst))
print("are_all_unique([1, 2, 3, 4]):", are_all_unique([1, 2, 3, 4]))
def are_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print("are_same_type([1, 2, 3]):", are_same_type([1, 2, 3]))
def is_valid_variable(var_name):
    return var_name.isidentifier() and not keyword.iskeyword(var_name)
print("is_valid_variable('my_var'):", is_valid_variable('my_var'))
sample_countries = [
    {'name': 'Finland', 'population': 5530719, 'languages': ['Finnish', 'Swedish']},
    {'name': 'Sweden', 'population': 10353442, 'languages': ['Swedish']},
    {'name': 'Nigeria', 'population': 206139589, 'languages': ['English']}
]
def most_spoken_languages(countries_data, limit=10):
    language_counts = {}
    for country in countries_data:
        for lang in country.get('languages', []):
            language_counts[lang] = language_counts.get(lang, 0) + 1
            
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return [(count, lang) for lang, count in sorted_languages[:limit]]
print("most_spoken_languages():", most_spoken_languages(sample_countries, limit=2))
def most_populated_countries(countries_data, limit=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:limit]]
print("most_populated_countries():", most_populated_countries(sample_countries, limit=20))