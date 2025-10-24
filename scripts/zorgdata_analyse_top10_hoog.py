# Zorgdata Analyse – Portfolio Project 3
# Auteur: Cedric
# Datum: [vandaag]

import pandas as pd

# 1. Pad naar het CSV-bestand
pad = r"C:\Users\cedri\Desktop\Power BI vacature\3) Python data project\data\kostenengebruikvanzorgnaarwet-gemeenten.csv"  # omdat het in dezelfde map staat

# 2. CSV inlezen
df = pd.read_csv(pad)

# 3. Controle: basisinfo
# print("Vorm van de dataset:", df.shape)  # (rijen, kolommen)
# print("\nKolomnamen:")
# print(df.columns.tolist())  # lijst van kolommen
# print("\nEerste 5 rijen:")
# print(df.head())  # eerste paar regels

df = df.set_index("Gemeente")

# 5. Alleen kolommen met 'Kosten' selecteren
kosten_kolommen = [col for col in df.columns if "Kosten" in col]
df_kosten = df[kosten_kolommen]

# 6. Totale zorgkosten per gemeente berekenen
df["Totale_zorgkosten"] = df_kosten.sum(axis=1)

# 7. Top 10 gemeenten met hoogste totale zorgkosten
top10 = df["Totale_zorgkosten"].sort_values(ascending=False).head(10)
print("\nTop 10 gemeenten met hoogste totale zorgkosten:")
print(top10)

# 8. Visualisatie van de top 10 gemeenten
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
top10.plot(kind="bar", color="skyblue")

plt.title("Top 10 gemeenten met hoogste totale zorgkosten (2014-2015)")
plt.xlabel("Gemeente")
plt.ylabel("Totale zorgkosten (in miljoenen €)")
plt.xticks(rotation=45, ha="right")

# Y-as formatteren (miljoenen)
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'€{x/1e6:,.0f}M'))

# ➕ Datalabels toevoegen
for i, value in enumerate(top10):
    plt.text(i, value + (0.01 * value), f'€{value/1e6:,.0f}M', 
             ha='center', va='bottom', fontsize=9, color='black')

plt.tight_layout()

plt.savefig("top10_zorgkosten_hoog.png", dpi=300)
plt.savefig("top10_zorgkosten_hoog.pdf", dpi=300)

plt.show()