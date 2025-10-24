# Zorgdata Analyse – Laagste 10 gemeenten
# Auteur: Cedric Kivits
# Datum: Oktober 2025

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 1. Inlezen van de dataset
pad = r"C:\Users\cedri\Desktop\Power BI vacature\3) Python data project\data\kostenengebruikvanzorgnaarwet-gemeenten.csv"
df = pd.read_csv(pad)

# 2. Gemeente als index
df = df.set_index("Gemeente")

# 3. Alleen kolommen met "Kosten" selecteren
kosten_kolommen = [col for col in df.columns if "Kosten" in col]
df_kosten = df[kosten_kolommen].apply(pd.to_numeric, errors="coerce")

# 4. Totale zorgkosten per gemeente
df["Totale_zorgkosten"] = df_kosten.sum(axis=1)

# 5. Top 10 laagste gemeenten
bottom10 = df["Totale_zorgkosten"].sort_values(ascending=True).head(10)
print("\nTop 10 gemeenten met laagste totale zorgkosten:")
print(bottom10)

# 6. Visualisatie
plt.figure(figsize=(10, 6))
bottom10.plot(kind="bar", color="lightcoral")

plt.title("Top 10 gemeenten met laagste totale zorgkosten (2014–2015)")
plt.xlabel("Gemeente")
plt.ylabel("Totale zorgkosten (in miljoenen €)")
plt.xticks(rotation=45, ha="right")

# Formatteren in miljoenen
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'€{x/1e6:,.0f}'.replace(',', '.') + 'M'))

# Datalabels boven de staven
for i, value in enumerate(bottom10):
    plt.text(i, value + (0.01 * value), f'€{value/1e6:,.0f}M', 
             ha='center', va='bottom', fontsize=9, color='black')

plt.tight_layout()

plt.savefig("top10_zorgkosten_laag.png", dpi=300)
plt.savefig("top10_zorgkosten_laag.pdf", dpi=300)

plt.show()