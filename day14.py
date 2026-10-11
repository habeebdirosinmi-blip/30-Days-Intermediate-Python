from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countries_data = [
    {
        'name': 'Afghanistan',
        'capital': 'Kabul',
        'population': 40462186,
        'languages': ['Pashto', 'Uzbek', 'Turkmen']
    },
    {
        'name': 'Finland',
        'capital': 'Helsinki',
        'population': 5530719,
        'languages': ['Finnish', 'Swedish']
    },
    {
        'name': 'Sweden',
        'capital': 'Stockholm',
        'population': 10416781,
        'languages': ['Swedish']
    },
    {
        'name': 'Estonia',
        'capital': 'Tallinn',
        'population': 1331057,
        'languages': ['Estonian']
    }
]
print("1. Map, Filter, Reduce Differences:")
print("   - map: Applies a function to every item in an iterable and returns a new iterable/map object.")
print("   - filter: Evaluates each item against a boolean condition function and keeps only those that return True.")
print("   - reduce: Applies a function cumulatively to items in an iterable, reducing the collection down to a single value.")
print("\n2. Higher Order Function, Closure, Decorator Differences:")
print("   - Higher Order Function: A function that can take other functions as parameters, return functions, or both.")
print("   - Closure: A nested function that retains access to variables from its enclosing outer function even after that outer function has finished executing.")
print("   - Decorator: A specialized higher-order function designed to wrap and extend the behavior of another function dynamically without modifying its source code.")
def square(x):
    return x ** 2
numbers_squared_example = list(map(square, numbers))
print("\nMap with defined function:", numbers_squared_example[:5])
print("Countries:")
for country in countries:
    print(country)
print("Names:")
for name in names:
    print(name)
print("Numbers:")
for num in numbers:
    print(num)
countries_upper = list(map(lambda c: c.upper(), countries))
print("Countries Upper:", countries_upper)
numbers_squared = list(map(lambda n: n ** 2, numbers))
print("Numbers Squared:", numbers_squared)
names_upper = list(map(lambda name: name.upper(), names))
print("Names Upper:", names_upper)
countries_not_six_chars = list(filter(lambda c: len(c) != 6, countries))
print("Not 6 chars:", countries_not_six_chars)
countries_less_than_six = list(filter(lambda c: len(c) < 6, countries))
print("Less than 6 chars:", countries_less_than_six)
countries_no_e = list(filter(lambda c: not c.startswith('E'), countries))
print("Without starting 'E':", countries_no_e)
chained_result = reduce(lambda x, y: x + y, filter(lambda x: x > 20, map(lambda x: x ** 2, numbers)))
print("Chained iterator result (sum of squares > 20):", chained_result)
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))
print("String items only:", get_string_lists([1, 'Apple', 2, 'Banana', True, 'Cherry']))
total_sum = reduce(lambda x, y: x + y, numbers)
print("Total sum:", total_sum)
sentence = reduce(lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y} are north European countries", countries)
print("Sentence:", sentence)
def categorize_countries(pattern, country_list):
    return list(filter(lambda c: pattern.lower() in c.lower(), country_list))
print("Categorize countries ('ia'):", categorize_countries('ia', ['Finland', 'Sweden', 'Russia', 'India']))
def get_first_ten_countries(country_list):
    return country_list[:10]
print("First 10 countries:", get_first_ten_countries(countries))
def get_last_ten_countries(country_list):
    return country_list[-10:]
print("Last 10 countries:", get_last_ten_countries(countries))
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("Sorted by Name:", [c['name'] for c in sorted_by_name])
print("Sorted by Capital:", [c['capital'] for c in sorted_by_capital])
print("Sorted by Population:", [(c['name'], c['population']) for c in sorted_by_population])
def most_spoken_languages(data):
    language_counts = {}
    for country in data:
        for lang in country.get('languages', []):
            language_counts[lang] = language_counts.get(lang, 0) + 1
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]
print("Most Spoken Languages:", most_spoken_languages(countries_data))
def most_populated_countries(data):
    sorted_pop = sorted(data, key=lambda x: x['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_pop[:10]]
print("Ten Most Populated Countries:", most_populated_countries(countries_data))