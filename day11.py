import math
import keyword
from collections import Counter
def add_two_numbers(a, b):
    return a + b
def area_of_circle(r):
    return math.pi * r * r
def add_all_nums(*args):
    total = 0
    for item in args:
        if not isinstance(item, (int, float)):
            return f"Error: All inputs must be numeric. Found invalid item: {item} ({type(item).__name__})"
        total += item
    return total

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def check_season(month):
    month = str(month).strip().capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    return 'Invalid month'
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
def print_list(lst):
    for item in lst:
        print(item)
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]
def add_item(lst, item):
    return lst + [item]
def remove_item(lst, item):
    return [x for x in lst if x != item]
def sum_of_numbers(n):
    return sum(range(1, n + 1))
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
def factorial(n):
    if n < 0:
        return "Factorial undefined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_empty(val):
    return not bool(val)
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def calculate_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def calculate_mode(lst):
    if not lst:
        return None
    counts = Counter(lst)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0

def calculate_variance(lst):
    if not lst:
        return 0
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
def greet(name="Guest"):
    return f"Hello, {name}!"
def show_args(**kwargs):
    formatted_args = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
    print(f"Received: {formatted_args}")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def all_unique(lst):
    return len(lst) == len(set(lst))

def same_data_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
def is_valid_variable(var_name):
    return var_name.isidentifier() and not keyword.iskeyword(var_name)
def most_spoken_languages(countries, top=10):
    language_counts = Counter()
    for country in countries:
        for lang in country.get('languages', []):
            language_counts[lang] += 1
    return language_counts.most_common(top)

def most_populated_countries(countries, top=10):
    sorted_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:top]]


if __name__ == "__main__":
    print("add_two_numbers(5, 7) =", add_two_numbers(5, 7))
    print("area_of_circle(10) =", area_of_circle(10))
    print("convert_celsius_to_fahrenheit(25) =", convert_celsius_to_fahrenheit(25))
    print("sum_of_numbers(5) =", sum_of_numbers(5))
    print("sum_of_even(10) =", sum_of_even(10))
    print("evens_and_odds(10) =")
    print(evens_and_odds(10))
    print("factorial(5) =", factorial(5))
    print("calculate_mean([1, 2, 3, 4, 5]) =", calculate_mean([1, 2, 3, 4, 5]))
    print("greet('Ada') =", greet('Ada'))
    print("is_prime(13) =", is_prime(13))
    print("same_data_type([1, 2, 3]) =", same_data_type([1, 2, 3]))
