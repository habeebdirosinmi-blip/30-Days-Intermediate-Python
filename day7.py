it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Length of it_companies:", len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Netflix', 'Tesla', 'Meta'])
it_companies.remove('IBM')
# remove() raises a KeyError if the item is not found, whereas discard() does not.
print("Updated it_companies:", it_companies)
a_union_b = A.union(B)
print("\nA union B:", a_union_b)
a_intersect_b = A.intersection(B)
print("A intersection B:", a_intersect_b)
print("Is A a subset of B?", A.issubset(B))
print("Are A and B disjoint?", A.isdisjoint(B))
join_a_b = A.union(B)
join_b_a = B.union(A)
sym_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", sym_diff)
del A
del B
age_set = set(age)
print("\nLength of age list:", len(age))
print("Length of age set:", len(age_set))
print("Is the list bigger?", len(age) > len(age_set))
# String: Immutable ordered sequence of characters.
# List: Mutable ordered sequence that allows duplicates.
# Tuple: Immutable ordered sequence that allows duplicates.
# Set: Mutable unordered collection of unique elements.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace('.', '').split()
unique_words = set(words)
print("Unique words count:", len(unique_words))
print("Unique words set:", unique_words)