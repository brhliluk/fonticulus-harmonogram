import markdown_strings

from timetable_parser import Event


def document_template(event: Event):
    text = f"""
{markdown_strings.header(event.name, 1)}\n
{markdown_strings.bold("Datum:")} {event.date}\n
{markdown_strings.bold("Čas:")} {event.start_time.strftime("%H:%M")} - {event.end_time.strftime("%H:%M")}\n
{markdown_strings.bold("Časová dotace:")} {str(event.get_length().seconds//3600) + ":" + str((event.get_length().seconds//60)%60).zfill(2)}\n
{markdown_strings.bold("Instruktoři:")} __{event.team[0]}__ {"+" if (len(event.team[1:]) > 0) else ""} {' + '.join(event.team[1:])}\n
"Pozorovatel:"\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Cíle programu:")}\n
{markdown_strings.bold("Kontext programu:")}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Fyzická náročnost (1-6):")}\n
{markdown_strings.bold("Psychická náročnost (1-6):")}\n
{markdown_strings.bold("Rizika:")}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Pomůcky a materiál:")}\n
{markdown_strings.bold("Prostředí:")}\n
Příprava (kdy):\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Poznámky:")}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Popis programu:")}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Přílohy a Zdroje:")}\n
{markdown_strings.horizontal_rule()}
{markdown_strings.bold("Hodnocení:")}\n
Hodnocení pozorovatele:\n
"""
    return text
