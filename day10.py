for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i)
    i += 1
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1
for i in range(1, 8):
    print("#" * i)
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()
for i in range(11):
    print(f"{i} x {i} = {i * i}")
tech = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech:
    print(item)
for i in range(0, 101, 2):
    print(i)
for i in range(1, 101, 2):
    print(i)
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}.")
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")
countries = ['Finland', 'Germany', 'Iceland', 'Sweden', 'Ireland', 'Thailand']
land_countries = []
for country in countries:
    if 'land' in country:
        land_countries.append(country)
print(land_countries)
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)
countries_data = [
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish'], 'population': 5540720},
    {'name': 'Germany', 'languages': ['German'], 'population': 83783942},
    {'name': 'China', 'languages': ['Chinese'], 'population': 1439323776},
    {'name': 'India', 'languages': ['Hindi', 'English'], 'population': 1380004385},
    {'name': 'United States', 'languages': ['English', 'Spanish'], 'population': 331002651}
]
languages_set = set()
for country in countries_data:
    for lang in country['languages']:
        languages_set.add(lang)
print(f"Total number of languages: {len(languages_set)}")
lang_counts = {}
for country in countries_data:
    for lang in country['languages']:
        lang_counts[lang] = lang_counts.get(lang, 0) + 1
sorted_langs = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)
print("Ten most spoken languages:", sorted_langs[:10])
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_10_populated = [{'country': c['name'], 'population': c['population']} for c in sorted_countries[:10]]
print("10 most populated countries:", top_10_populated)