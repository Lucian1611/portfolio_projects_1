import csv


def write_csv(row):
    with open('date_sortare.csv', 'a', newline="") as csvfile:
        spamwriter = csv.writer(csvfile,
                                quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)
        # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


if __name__ == '__main__':
    write_csv(["Insert Sort", 14, 12.9])
