\# 🩺 Vermeidbare Sterblichkeit (Deutschland) – Indikator 3.1.a



Diese Analyse betrachtet die \*\*durch Prävention und Behandlung vermeidbare Sterblichkeit\*\* je 100.000 Einwohner\*innen (<75 Jahre).

\*\*Ziel:\*\* Senkung auf \*\*≤ 200\*\* bis \*\*2030\*\*.



\## 📊 Visuals (werden nach Skriptlauf angezeigt)



<p align="center">

&nbsp; <img src="assets/trend\_vermeidbare\_sterblickeit.png" alt="Trend vs Ziel" width="75%">

</p>

<p align="center">

&nbsp; <img src="assets/bar\_vermeidbare\_sterblickeit.png" alt="Jahreswerte" width="75%">

</p>

<p align="center">

&nbsp; <img src="assets/trend\_mit\_rolling\_mean.png" alt="Trend (Rolling Mean)" width="75%">

</p>



\## ▶️ Quickstart



```bash

cd ~/projects/Vermeidbare-Sterblichkeit-DE

python -m venv .venv

\# Git Bash:

source .venv/Scripts/activate

pip install -r requirements.txt



\# CSV in data/ legen (z. B. data/vermeidbare\_sterblickeit.csv)

python src/make\_plots.py



