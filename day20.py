import re
from collections import Counter
from statistics import mean, median
from bs4 import BeautifulSoup
import numpy as np
import requests


def parse_range(range_str):
    """Helper function to extract min, max, and mean from a metric/lifespan range string."""
    try:
        parts = [float(p.strip()) for p in range_str.split("-")]
        if len(parts) == 2:
            return parts[0], parts[1], mean(parts)
        elif len(parts) == 1:
            return parts[0], parts[0], parts[0]
    except Exception:
        pass
    return None, None, None


def exercise_1():
    
    url = "https://www.gutenberg.org/files/1112/1112.txt"
    response = requests.get(url)
    words = re.findall(r"\b[a-zA-Z]+\b", response.text.lower())
    word_counts = Counter(words)

    for word, count in word_counts.most_common(10):
        print(f"  {word}: {count}")
    print()
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, headers={"x-api-key": "DEMO-API-KEY"}, timeout=30)
    response.raise_for_status()
    breeds = response.json()

    weights = []
    lifespans = []
    country_breed_data = []

    for breed in breeds:
        if "weight" in breed and "metric" in breed["weight"]:
            min_w, max_w, _ = parse_range(breed["weight"]["metric"])
            if min_w is not None and max_w is not None:
                weights.extend([min_w, max_w])
        if "life_span" in breed:
            min_l, max_l, _ = parse_range(breed["life_span"])
            if min_l is not None and max_l is not None:
                lifespans.extend([min_l, max_l])
        origin = breed.get("origin")
        name = breed.get("name")
        if origin and name:
            country_breed_data.append((origin, name))
    print("Weight Stats (Metric):")
    print(
        f"  Min: {min(weights)} | Max: {max(weights)} | Mean: {mean(weights):.2f} | Median: {median(weights)} | Std Dev: {np.std(weights):.2f}"
    )
    print("Lifespan Stats (Years):")
    print(
        f"  Min: {min(lifespans)} | Max: {max(lifespans)} | Mean: {mean(lifespans):.2f} | Median: {median(lifespans)} | Std Dev: {np.std(lifespans):.2f}"
    )
    country_freq = Counter([item[0] for item in country_breed_data])
    print("Top Countries by Cat Breed Count:")
    for country, count in country_freq.most_common(5):
        print(f"  {country}: {count} breeds")
    print()
    url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    countries = response.json()
    largest_countries = sorted(
        countries, key=lambda x: x.get("area", 0), reverse=True
    )[:10]
    print("10 Largest Countries by Area:")
    for c in largest_countries:
        print(
            f"  - {c.get('name', {}).get('common')}: {c.get('area', 0):,} km²"
        )
    all_languages = []
    for c in countries:
        langs = c.get("languages", {})
        if langs:
            all_languages.extend(langs.values())

    lang_counter = Counter(all_languages)
    print(f"\nTotal number of unique languages: {len(lang_counter)}")
    print("10 Most Spoken Languages:")
    for lang, count in lang_counter.most_common(10):
        print(f"  - {lang} (spoken in {count} countries)")
    print()

    url = "https://archive.ics.uci.edu/datasets"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    datasets = soup.find_all("h2")

    print("Sample Datasets found on UCI:")
    count = 0
    for ds in datasets:
        text = ds.get_text(strip=True)
        if text:
            print(f"  - {text}")
            count += 1
            if count >= 10:
                break

