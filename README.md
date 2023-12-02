# Race Calendars

## Overview

This repository contains race calendars for various motorsport events. It aims to provide an easy way to keep track of race schedules for different categories.
I've also developed a Python [script](/pycsv2ics/src/main.py) that creates ics calendar files from CSV data.  

Check the [changelog](CHANGELOG.md) for the latest changes.

## Calendars Included

**2024:**
- Supercross
- AMA National Motocross  

**2023:**

- Formula 1
- MotoGP

## Calendar usage

Each calendar is provided in the iCalendar (.ics) format, which is compatible with most calendar applications. To use a calendar, simply download the corresponding .ics file and import it into your calendar application.


## Python script usage

Install dependencies

    pip install ics

Generate all (everything in /csv/)

    python main.py
or  generate a specific calendar

    python main.py calendar_name

## Contributing

Contributions are welcome! If you have updates to a calendar or want to add a new one, please feel free to make a pull request.

## License

[MIT](LICENSE)

## Reporting issues

If you have any questions or suggestions, please open an issue on GitHub.

