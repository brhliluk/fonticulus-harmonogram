from markdown import markdown

import file_uploader
from auth import auth
from folder_creator import create_folder
from template import document_template
from timetable_parser import get_timetable_events
from tqdm import tqdm

drive = auth()
timetable = get_timetable_events("timetable.csv")
folder_id = create_folder(drive, "PROGRAMY")
for event in tqdm(timetable.values()):
    text = document_template(event)
    htmldoc = markdown(text)
    file_uploader.upload(htmldoc, drive, folder_id, event.name)
