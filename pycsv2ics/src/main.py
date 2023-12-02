import csv
import os
from ics import Calendar, Event
from datetime import datetime
from pytz import timezone

def create_ics_from_csv(calendar_name):
    csv_path = f'./csv/{calendar_name}.csv'
    ics_path = f'./ics/{calendar_name}.ics'

    # If the ics file already exists, delete it
    if os.path.exists(ics_path):
        os.remove(ics_path)

    cal = Calendar()

    event_count = 0
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header
        for row in reader:
            event = Event()
            event.name = row[0]
            event.begin = timezone('Europe/London').localize(datetime.strptime(row[1], '%Y-%m-%d %H:%M'))
            event.end = timezone('Europe/London').localize(datetime.strptime(row[2], '%Y-%m-%d %H:%M'))
            event.location = row[3]
            event.created = datetime.now(timezone('Europe/London'))  # Add DTSTAMP property
            cal.events.add(event)
            event_count += 1

    ics_content = str(cal)
    ics_content = ics_content.replace('\r\n', '\n')  # Remove extra empty lines

    with open(ics_path, 'w') as ics_file:
        ics_file.write(ics_content)

    print(f'Processed file: {csv_path}, {len(cal.events)}/{event_count} events generated on {ics_path}')

def main(calendar_name=None):
    if calendar_name:
        create_ics_from_csv(calendar_name)
    else:
        for file in os.listdir('./csv'):
            if file.endswith('.csv'):
                create_ics_from_csv(file[:-4])  # Remove the .csv extension

if __name__ == "__main__":
    main()