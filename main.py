import pandas as pd
from bs4 import BeautifulSoup

all_names = []
all_summary = []
for i in range(1, 37):
    with open(f"data/Pokemon_{i}.html",encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    h2_withA = soup.find_all("h2",attrs={"class":"entry-title"})

    name = [h2.get_text(strip=True) for h2 in h2_withA]

    mary = soup.find_all("div", attrs={"class":"entry-summary"})
    summary = [sums.get_text(strip=True) for sums in mary]

    all_names.extend(name)
    all_summary.extend(summary)

df = pd.DataFrame({
    "Pokemon": all_names,
    "Description": all_summary
})
df.to_csv("Pokemon.csv", index=False)
print("Succusful")