# import csv
#
# albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
#           ("Bad Company", "Bad Company", 1974),
#           ("Nightflight", "Budgie", 1981),
#           ("More Mayhem", "Imelda May", 2011),
#           ("Ride the Lightning", "Metallica", 1984),
#           ]
#
# keys = ['album', 'artist', 'year']
#
# filename = 'albums.csv'
# with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=keys)
#     writer.writeheader()
#     for row in albums:
#         zip_object = zip(keys, row)
#         # print(zip_object)
#         # for thing in zip(keys, row):
#         #     print("\t", thing)
#         albums_dict = dict(zip_object)
#         print(albums_dict)
#         writer.writerow(albums_dict)


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    split = invoice_number.split('-')
    return tuple(int(num) for num in split)


print(parse_invoice_number('2019-0005'))