import csv

from datetime import datetime

from .functions import check_valid_ad_range, check_valid_bs_range
from .nepdate import NepDate


def check_date_format(date_string):
    date = date_string.split("-")

    # is there a year, month, and day component to the date?
    if len(date) != 3:
        return None

    # are all the components numbers?
    try:
        date[0] = int(date[0])
        date[1] = int(date[1])
        date[2] = int(date[2])
    except ValueError:
        return None

    return date


def english_to_nepali(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)

        with open('output_e2n.csv', 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["English Date", "Nepali Date"])

            for row in reader:
                english_date = None

                # check if the date is in the correct format
                try:
                    english_date = datetime.strptime(row[0], "%Y-%m-%d").date()
                except ValueError:
                    writer.writerow([row[0], "Invalid date"])
                    continue

                # check if the date is in the correct range
                try:
                    check_valid_ad_range(english_date)
                except ValueError:
                    writer.writerow([english_date, "Out of range"])
                    continue

                # since the date has passed all checks, convert the date and write it to the output file
                writer.writerow([english_date, NepDate.from_ad_date(english_date).date])


def nepali_to_english(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)

        with open('output_n2e.csv', 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Nepali Date", "English Date"])

            for row in reader:
                # check if the date is in the correct format
                nepali_date = check_date_format(row[0])

                if not nepali_date:
                    writer.writerow([row[0], "Invalid date"])
                    continue
                else:
                    nepali_date = NepDate(nepali_date[0], nepali_date[1], nepali_date[2])

                # check if the date is in the correct range
                try:
                    check_valid_bs_range(nepali_date)
                except ValueError:
                    writer.writerow([nepali_date.date, "Out of range"])
                    continue

                # generate the english date
                nepali_date.update()

                # since the date has passed all checks, convert the date and write it to the output file
                writer.writerow([nepali_date.date, nepali_date.en_date.strftime("%Y-%m-%d")])
