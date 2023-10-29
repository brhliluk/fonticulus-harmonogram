# fonticulus-harmonogram
Python utilita, která rozparsuje harmonogram z csv souboru a vytvoří programové listy

## Setup
  - Podle (návodu)[https://ericmjl.github.io/blog/2023/3/8/how-to-automate-the-creation-of-google-docs-with-python/], popsaném v prvních dvou bodech si vytvořte servisní účet na google cloud a nastavte si přístup ke google disku.
  - Nahraďte soubor `timetable.csv` harmonogramem, který chcete rozdělit do programových listů. Harmonogram musí dodržovat stanovený formát viz. formát.
  - Nainstalujte si potřebné knihovny pomocí `pip install PyDrive2 pyprojroot dotenv markdown markdown_strings datetime pandas`

## Používání
  - Spusťte parser pomocí příkazu `python main.py`
  - Na výstupu dostanete odkaz na složku, kam se budou postupně nahrávat programové listy.
  - Jednotlivé google dokumenty je potřeba ze složky pomocí `CTRL+C` a `CTRL+V` vykopírovat - využití jiných způsobů bohužel překáží vlastnictví souborů vytvořeným Google cloud service účtem.

## Formát harmonogramu
  - Řídit se můžete přiloženým nahraným harmonogramem (harmonogram 2023.xlsx/timetable.csv)
  - Jako program, pro který se vytváří programový list se považuje buňka, která obsahuje levou i pravou závorku.
  - Jako datum programu se považuje první buňka řádku.
  - Počáteční čas programu je první sloupec, ve kterém se nachází.
  - Konečný čas programu je počáteční čas dalšího programu, nebo počáteční čas jedné z opakujících se událostí (oběd/svačina/večeře/reflexe/rituál). Pokud po programu nenásleduje v daném dni už nic, je jeho konečným časem 23:59:59.
  - Instruktoři vedoucí daný program jsou uvedeni v závorce.
  - V případě, že buňka obsahuje ',' - předpokládá se že jimi jsou odděleny jednotlivé programy, které probíhají ve stejný čas.
  - V případě shody názvu programů se vezme počáteční čas z prvního a konečný čas z dalšího.