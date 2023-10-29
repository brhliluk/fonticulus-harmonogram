import markdown_strings

from timetable_parser import Event


def document_template(event: Event):
    text = f"""
{markdown_strings.header("Základní informace:", 1)}\n
{markdown_strings.bold("Název programu:")} {event.name}\n
{markdown_strings.bold("Datum:")} {event.date}\n
{markdown_strings.bold("Čas:")} {event.start_time.time()} - {event.end_time.time()}\n
{markdown_strings.bold("Časová dotace:")} {event.get_length()}\n
{markdown_strings.bold("Instruktoři:")} {event.team}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Pomůcky a materiál, prostředí:")}\n
Příprava (kdy):\n
Příprava (co):\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Fyzická náročnost (1-6):")}\n
{markdown_strings.bold("Psychická náročnost (1-6):")}\n
{markdown_strings.bold("Rizika:")}\n

Cíle programu:\n
\n

Kontext programu:\n
\n

Příprava ({markdown_strings.bold("Zápisy z porad, nápady, rozdělení toho co kdo připravuje…")})\n
\n

Popis programu ({markdown_strings.bold("Popis průběhu, pravidla her, návody, techniky, metody…")})\n

{markdown_strings.horizontal_rule()}
Přílohy a Zdroje:\n

{markdown_strings.horizontal_rule()}
Hodnocení ({markdown_strings.bold("Moje hodnocení, sebereflexe a doporučení pro příště…")})\n

Hodnocení pozorovatele:\n
"""
    return text
