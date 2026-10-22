import pandas as pd
url = 'https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/hacker_news.csv'
df = pd.read_csv(url)
print("FIRST 5 ROWS")
print(df.head())
print("\nLAST 5 ROWS")
print(df.tail())
titles = df['title']
print("\nTITLE SERIES (First 5)")
print(titles.head())
print("\nNUMBER OF ROWS AND COLUMNS")
print(df.shape) 
python_titles = df[df['title'].str.contains('python', case=False, na=False)]
print(f"\nTITLES CONTAINING 'PYTHON' ({len(python_titles)} found)")
print(python_titles['title'].head())
js_titles = df[df['title'].str.contains('javascript', case=False, na=False)]
print(f"\nTITLES CONTAINING 'JAVASCRIPT' ({len(js_titles)} found)")
print(js_titles['title'].head())
print("\nDATA SUMMARY")
print(df.info())