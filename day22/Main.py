import json
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


url_bu = (
    "https://www.bu.edu/president/boston-university-facts-stats/"
)

try:
  response_bu = requests.get(url_bu, headers=HEADERS)
  soup_bu = BeautifulSoup(response_bu.content, "html.parser")

  bu_data = {}
  headings = soup_bu.find_all(["h2", "h3", "h4"])

  for heading in headings:
    title = heading.get_text(strip=True)
    items = []
    for sibling in heading.find_next_siblings():
      if sibling.name in ["h2", "h3", "h4"]:
        break
      if sibling.name in ["p", "ul", "li", "div"]:
        text = sibling.get_text(strip=True)
        if text:
          items.append(text)
    if items:
      bu_data[title] = items

  with open("bu_facts.json", "w", encoding="utf-8") as f:
    json.dump(bu_data, f, ensure_ascii=False, indent=4)
  print("Correct\n")
except Exception as e:
  print(f"Failed {e}\n")


url_uci = "https://archive.ics.uci.edu/ml/datasets.php"

try:
  response_uci = requests.get(url_uci, headers=HEADERS)
  soup_uci = BeautifulSoup(response_uci.content, "html.parser")

  datasets = []
  
  tables = soup_uci.find_all("table", {"cellpadding": "3"})

  if tables:
    table = tables[0]
    rows = table.find_all("tr")
    for row in rows:
      cols = row.find_all(["td", "th"])
      cols = [ele.text.strip() for ele in cols]
      if cols:
        datasets.append(cols)

  
  if not datasets:
    for tr in soup_uci.find_all("tr"):
      cols = [ele.text.strip() for ele in tr.find_all(["td", "th"])]
      if cols:
        datasets.append(cols)

  with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(datasets, f, ensure_ascii=False, indent=4)
  print(f"Correct ({len(datasets)} rows found)\n")
except Exception as e:
  print(f"Failed {e}\n")



url_wiki = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

try:
  response_wiki = requests.get(url_wiki, headers=HEADERS)
  soup_wiki = BeautifulSoup(response_wiki.content, "html.parser")

  tables = soup_wiki.find_all("table", {"class": "wikitable"})
  presidents = []

  if tables:
    table_wiki = tables[0]
    rows = table_wiki.find_all("tr")
    for row in rows:
      cols = row.find_all(["td", "th"])
      cols = [ele.text.strip() for ele in cols]
      if cols:
        presidents.append(cols)

  with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, ensure_ascii=False, indent=4)
  print(f"Correct ({len(presidents)} rows found)\n")
except Exception as e:
  print(f"Failed: {e}\n")

print("And done")