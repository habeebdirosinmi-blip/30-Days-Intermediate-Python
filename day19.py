import os
import json
import csv
import re
from collections import Counter


data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

speeches = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]
for speech in speeches:
    file_path = os.path.join(data_folder, speech)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f" {speech} -> Lines: {len(lines)}, Words: {sum(len(l.split()) for l in lines)}")
    else:
        print(f"Could not find: {file_path}")

json_file = 'data/countries_data.json'
if not os.path.exists(json_file):
    print(f" Critical Error: Could not find '{json_file}'. Make sure your 'data' folder contains 'countries_data.json'!")
else:
    print(f" Found '{json_file}' successfully!\n")

    
    def most_spoken_languages(filename, top_n):
        with open(filename, 'r', encoding='utf-8') as f:
            countries = json.load(f)
            
        language_counter = Counter()
        for country in countries:
            for language in country.get('languages', []):
                language_counter[language] += 1
                
        return [(count, lang) for lang, count in language_counter.most_common(top_n)]

    print("Top 3 Most Spoken Languages:")
    print(most_spoken_languages(filename=json_file, top_n=3))
    print("\n")


    
    def most_populated_countries(filename, top_n):
        with open(filename, 'r', encoding='utf-8') as f:
            countries = json.load(f)
        sorted_countries = sorted(countries, key=lambda x: x.get('population', 0), reverse=True)
        
        result = [{'country': c.get('name'), 'population': c.get('population')} for c in sorted_countries[:top_n]]
        return result

    print("Top 3 Most Populated Countries:")
    print(json.dumps(most_populated_countries(filename=json_file, top_n=3), indent=4))
def extract_emails(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return list(set(re.findall(email_pattern, content)))
emails_sample = extract_emails('data/email_exchange_big.txt')
print(f"Total unique emails found: {len(emails_sample)}")
print()
def find_most_common_words(source, top_n):
    if os.path.exists(source):
        with open(source, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = source
        
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(top_n)
print("Obama's Top 5 Words:", find_most_common_words('data/obama_speech.txt', 5))
print("Michelle's Top 5 Words:", find_most_common_words('data/michelle_obama_speech.txt', 5))
print()
def load_stop_words(filepath):
    if not os.path.exists(filepath):
        return set()
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(line.strip().lower() for line in f if line.strip())

def clean_and_tokenize(text_or_file, stop_words=None):
    if os.path.exists(text_or_file):
        with open(text_or_file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = text_or_file
        
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if stop_words:
        words = [w for w in words if w not in stop_words]
    return set(words)

def check_text_similarity(source1, source2, stop_words_file='data/stop_words.py'):
    stop_words = load_stop_words(stop_words_file)
    set1 = clean_and_tokenize(source1, stop_words)
    set2 = clean_and_tokenize(source2, stop_words)
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return (intersection / union) * 100 if union > 0 else 0
similarity = check_text_similarity('data/michelle_obama_speech.txt', 'data/melina_trump_speech.txt')
print(f"Similarity Score: {similarity:.2f}%")
print()
romeo_file = 'data/romeo_and_juliet.txt'
if os.path.exists(romeo_file):
    top_words = find_most_common_words(romeo_file, 10)
    print(top_words)
else:
    print(f" Missing file: {romeo_file}. Make sure 'romeo_and_juliet.txt' is placed inside your local 'data' folder.")
def analyze_hacker_news(filename):
    if not os.path.exists(filename):
        print(f"Missing file: {filename}")
        return
        
    python_count = 0
    js_count = 0
    java_only_count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            row_text = " ".join(row)
            if re.search(r'\bpython\b', row_text, re.IGNORECASE):
                python_count += 1
            if re.search(r'\bjavascript\b', row_text, re.IGNORECASE):
                js_count += 1
            
            has_java = re.search(r'\bjava\b', row_text, re.IGNORECASE)
            has_js = re.search(r'\bjavascript\b', row_text, re.IGNORECASE)
            if has_java and not has_js:
                java_only_count += 1
                
    print(f"Python mentions: {python_count}")
    print(f"JavaScript mentions: {js_count}")
    print(f"Java (excluding JavaScript) mentions: {java_only_count}")
analyze_hacker_news('data/hacker_news.csv')