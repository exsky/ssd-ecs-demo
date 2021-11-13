import csv


def fetch_staff_info(staff):
    with open('statics/staff.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rowdict = dict(zip(header, row))
            if rowdict['account_id'] == staff:
                return rowdict
