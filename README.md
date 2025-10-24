Zorgdata Analyse – Gemeentelijke Zorgkosten (2014–2015)

Auteur: Cedric Kivits
Datum: Oktober 2025
Taal: Python 3 (pandas, matplotlib)

------------------------------------------------------------------
Beschrijving

Dit project analyseert de totale zorgkosten per gemeente in Nederland op basis van data uit de open dataset “Kosten en gebruik van zorg naar wet (gemeenten)” van het CBS.
De dataset bevat informatie over kosten per zorgcategorie, zoals huisartsenzorg, farmaceutische zorg, langdurige zorg (WLZ) en geestelijke gezondheidszorg (GGZ).

* Het doel van deze analyse is om inzicht te krijgen in:
* Gemeenten met de hoogste totale zorgkosten
* Gemeenten met de laagste totale zorgkosten
* Gebruikte technieken
* pandas – datamanipulatie (inlezen, filteren, aggregeren)
* list comprehension – kolommen selecteren op naam ("Kosten")
* sum(axis=1) – berekenen van totale zorgkosten per gemeente
* matplotlib – visualisatie van de Top 10 (hoogste en laagste gemeenten)
* FuncFormatter – opmaak van bedragen in miljoenen euro’s
* Data labels – bedragen boven de staven voor leesbaarheid

------------------------------------------------------------------
Resultaten

Er zijn twee scripts:

* zorgdata_analyse_top10_hoog.py
* Toont de tien gemeenten met de hoogste totale zorgkosten.

* zorgdata_analyse_top10_laag.py
* Toont de tien gemeenten met de laagste totale zorgkosten.

Beide scripts produceren een staafdiagram met bedragen in miljoenen euro’s.

De resultaten geven een duidelijk beeld van de verdeling van zorgkosten in Nederland.
Grote steden zoals Amsterdam en Rotterdam hebben de hoogste totale zorgkosten,
terwijl kleinere gemeenten aanzienlijk lagere totale uitgaven laten zien.

------------------------------------------------------------------
Output

* top10_zorgkosten_hoog.png
* top10_zorgkosten_laag.png

------------------------------------------------------------------
Lessen en vaardigheden

* Werken met open data van de overheid
* Data cleaning en filtering met Python
* Visualiseren en formatteren van financiële data
* Interpreteren van maatschappelijke datasets

------------------------------------------------------------------
Bron
* Dataset: Kosten en gebruik van zorg naar wet (gemeenten) – CBS / Overheid.nl