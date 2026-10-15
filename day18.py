from collections import Counter
import re
paragraph = 'I love teaching . If you do not love teaching what else can you love . I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love .'
words = re.findall(r'\b[A-Za-z]+\b', paragraph)
word_counts = Counter(words)
print(word_counts.most_common())
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = [int(n) for n in re.findall(r'-?\d+', text)]
sorted_points = sorted(points)
distance = max(sorted_points) - min(sorted_points)
print('Points:', sorted_points)
print('Distance:', distance)  
def is_valid_variable(var_name):
  pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
  return bool(re.match(pattern, var_name))
print(is_valid_variable('first_name'))  
print(is_valid_variable('first-name'))  
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))  
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(text):
  cleaned = re.sub(r'[^A-Za-z0-9 ]+', '', text)
  return re.sub(r'\s+', ' ', cleaned).strip()
def most_frequent_words(text):
  words = text.split()
  return Counter(words).most_common(3)
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))