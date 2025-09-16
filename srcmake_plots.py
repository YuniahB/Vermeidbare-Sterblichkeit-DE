import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = "data"
ASSETS_DIR = "assets"

# ==== CSV-Dateiname anpassen! ====
CSV_NAME = "vermeidbare_sterblickeit.csv"  # benenne deine Datei so oder ändere hier

csv_path = os.path.join(DATA_DIR, CSV_NAME)
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV nicht gefunden unter {csv_path}. Bitte Datei in data/ ablegen und Namen in src/make_plots.py prüfen.")

# robustes Einlesen
df = None
for enc in ["utf-8", "latin1"]:
    for sep in [";", ","]:
        try:
            tmp = pd.read_csv(csv_path, sep=sep, encoding=enc)
            if tmp.shape[1] >= 2:
                df = tmp
                break
        except Exception:
            pass
    if df is not None:
        break

if df is None:
    raise ValueError("CSV konnte nicht geparst werden. Bitte Trennzeichen/Encoding prüfen.")

df.columns = [str(c).strip() for c in df.columns]

# Spalten-Heuristik
year_col = None
value_col = None
for c in df.columns:
    lc = c.lower()
    if lc in ["year", "jahr", "jahrgang"]:
        year_col = c
    if lc in ["value", "wert", "indikatorwert", "rate", "zahl"]:
        value_col = c
if year_col is None:
    year_col = df.columns[0]
if value_col is None:
    value_col = df.columns[-1]

df[year_col] = pd.to_numeric(df[year_col], errors="coerce")
df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
df = df.dropna(subset=[year_col, value_col]).sort_values(year_col)

years = df[year_col].values
values = df[value_col].values

os.makedirs(ASSETS_DIR, exist_ok=True)

# Plot 1: Trend mit Ziel-Linie 200
plt.figure(figsize=(8,5))
plt.plot(years, values, marker="o")
plt.axhline(200, linestyle="--")
plt.title("Vermeidbare Sterblichkeit – Trend")
plt.xlabel("Jahr")
plt.ylabel("Todesfälle je 100.000 (<75)")
plt.tight_layout()
plt.savefig(os.path.join(ASSETS_DIR, "trend_vermeidbare_sterblickeit.png"))
plt.close()

# Plot 2: Balken
plt.figure(figsize=(8,5))
plt.bar(years, values)
plt.axhline(200, linestyle="--")
plt.title("Vermeidbare Sterblichkeit – Jahreswerte")
plt.xlabel("Jahr")
plt.ylabel("Todesfälle je 100.000 (<75)")
plt.tight_layout()
plt.savefig(os.path.join(ASSETS_DIR, "bar_vermeidbare_sterblickeit.png"))
plt.close()

# Plot 3: Rolling Mean (3 Jahre)
s = pd.Series(values, index=years)
rm = s.rolling(3, min_periods=1).mean()
plt.figure(figsize=(8,5))
plt.plot(s.index, s.values, marker="o")
plt.plot(rm.index, rm.values, linestyle="-.")
plt.axhline(200, linestyle="--")
plt.title("Vermeidbare Sterblichkeit – Trend & 3J Gleitmittel")
plt.xlabel("Jahr")
plt.ylabel("Todesfälle je 100.000 (<75)")
plt.tight_layout()
plt.savefig(os.path.join(ASSETS_DIR, "trend_mit_rolling_mean.png"))
plt.close()

print("✅ Plots gespeichert unter:", ASSETS_DIR)
