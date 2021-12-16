
import csv
import os
import sys


def csv_writer(data, header, output_directory, name=None):
    if name is None:
        name = "output.csv"

    if sys.version_info < (3, 0):
        with open(os.path.join(output_directory, name), "wb") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            writer.writerows(data)
    else:
        with open(os.path.join(output_directory, name), "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            writer.writerows(data)


def csv_reader(f_path):
    if sys.version_info < (3, 0):
        with open(f_path, "rb") as csvfile:
            reader = csv.reader(csvfile)

            return list(reader)
    else:
        with open(f_path, newline="") as csvfile:
            reader = csv.reader(csvfile)

            return list(reader)


def unicode_csv_dict_writer(data, header, output_directory, name=None):
    try:
        import unicodecsv
    except ImportError:
        print("[+] Install unicodecsv module before executing this function")
        sys.exit(1)

    if name is None:
        name = "output.csv"

    print("[+] Writing {} to {}".format(name, output_directory))
    with open(os.path.join(output_directory, name), "wb") as csvfile:
        writer = unicodecsv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

        writer.writerows(data)
