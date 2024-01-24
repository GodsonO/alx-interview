#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_statcode: dict of status codes
        total_filesize: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_filesize))
    for key, val in sorted(dict_statcode.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_filesize = 0
code = 0
counter = 0
dict_statcode = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_filesize += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_statcode.keys()):
                    dict_statcode[code] += 1

            if (counter == 10):
                print_msg(dict_statcode, total_filesize)
                counter = 0

finally:
    print_msg(dict_statcode, total_filesize)
