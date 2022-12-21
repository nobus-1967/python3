# Generate date in a specific period.
from datetime import datetime
from random import randrange


def main():
    start_date_input = input(
        'Enter 1st date in format YYYY/MM/DD:  '
    )
    end_date_input = input(
        'Enter 2nd date in format YYYY/MM/DD:  '
    )

    start_year, start_month, start_day = tuple(
        map(int, start_date_input.split('/'))
    )
    start_date = datetime(
        start_year, start_month, start_day
    )
    start_date_secs = int(start_date.timestamp())

    end_year, end_month, end_day = tuple(
        map(int, end_date_input.split('/'))
    )
    end_date = datetime(
        end_year, end_month, end_day
    )
    end_date_secs = int(end_date.timestamp())

    middle_date_secs = randrange(
        start_date_secs, end_date_secs
    )
    middle_date = datetime.fromtimestamp(
        middle_date_secs
    )
    print(
        'Generated date (between 1st and 2nd):',
        f"{middle_date.strftime('%Y/%m/%d')}",
    )


if __name__ == '__main__':
    main()
