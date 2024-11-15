import pandas as pd
from datetime import datetime

DAY_END = datetime.strptime("23:59:59", "%H:%M:%S")


class Event:
    def __init__(self, name: str, date, start_time, end_time=DAY_END):
        split_name = name.replace("\n", " ").split(' (')
        self.name = split_name[0]
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.team = split_name[1].removesuffix(')').split(' + ')

    def get_length(self):
        return self.end_time - self.start_time


def extract_event_info(row):
    date = row[0]
    timetable_events = []
    regular_events = ['OBĚD', 'SVAČINA', 'VEČEŘE', 'REFLEXE', 'RITUÁL']

    for column, item in row.items():
        # Init all event info
        if isinstance(item, str) and '(' in item and ')' in item:
            try:
                time = datetime.strptime(column, "%H:%M")
            except (ValueError, TypeError):
                time = DAY_END
            # Multiple simultaneous events at the same time
            if ',' in item:
                detailed = item.split(',')
                for detail in detailed:
                    timetable_events.append(Event(detail, date, time))
            else:
                timetable_events.append(Event(item, date, time))

        # Set end times for previous event in timetable if this event is regular (does not need own file)
        if isinstance(item, str) and len(timetable_events) != 0:
            if any(ele in item for ele in regular_events):
                try:
                    new_end_time = datetime.strptime(column, "%H:%M")
                except (ValueError, TypeError):
                    break
                # Two regular events next to each other, we need the first one
                if new_end_time < timetable_events[len(timetable_events) - 1].end_time:
                    j = 1
                    while timetable_events[len(timetable_events) - 1].start_time == timetable_events[len(timetable_events) - j].start_time:
                        timetable_events[len(timetable_events) - j].end_time = new_end_time
                        if len(timetable_events) == j:
                            break
                        else:
                            j += 1

    # Set end times for the rest
    for i in range(len(timetable_events)):
        if timetable_events[i].end_time != DAY_END:
            continue
        if i == (len(timetable_events) - 1):
            timetable_events[i].end_time = DAY_END
        else:
            j = 1
            while timetable_events[i].start_time == timetable_events[i + j].start_time:
                j += 1
            timetable_events[i].end_time = timetable_events[i + j].start_time

    return timetable_events


def get_timetable_events(file_path):
    events = {}

    timetable = pd.read_csv(file_path)
    # Iterate through the DataFrame and extract event information
    for index, row in timetable.iterrows():
        for event in extract_event_info(row):
            if event.name in events:
                events[event.name].end_time = event.end_time
            else:
                events[event.name] = event

    # Print all extracted event names, dates, and times
    # for key, event in events.items():
    #     print(f"Event: {event.name}")
    #     print(f"Date: {event.date}")
    #     print(f"Start Time: {event.start_time.time()}")
    #     print(f"End Time: {event.end_time.time()}")
    #     print(f"Length: {event.get_length()}")
    #     print(f"Team: {event.team}")
    #     print("---------")
    return events
