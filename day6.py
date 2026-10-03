empty_tuple = ()
brothers = ("Haseeb", "Rayan")
sisters = ("Aishat", "Semiat")
siblings = brothers + sisters
print("Siblings:", siblings)
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)
parents = ("Jide", "Nimota")
family_members = siblings + parents
print("Family Members:", family_members)
*siblings_unpacked, father, mother = family_members
print("Unpacked siblings:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)
fruits = ("Watermelon", "Guava", "Pawpaw")
vegetables = ("Carrot", "Okra", "Cucumber")
animal_products = ("Honey", "Eggs", "Butter")
food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
n = len(food_stuff_lt)
if n % 2 == 1:
    middle_items = food_stuff_lt[n // 2]
else:
    middle_items = food_stuff_lt[(n // 2) - 1 : (n // 2) + 1]
print("Middle item(s):", middle_items)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)
del food_stuff_tp
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Is Estonia a nordic country?", "Estonia" in nordic_countries)
print("Is Iceland a nordic country?", "Iceland" in nordic_countries)
6