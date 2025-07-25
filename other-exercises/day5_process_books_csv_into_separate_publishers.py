#!/usr/bin/env python

# using the dataset under `books.csv`:
# [x] - read the csv
# [x] - write out separate files for each publisher,
#       named "books_Publisher_<publisher_name>.csv".
#
# extra-requirements:
# [x] a) skip the "Publisher" column in the output.
# [x] b) if the Publisher is empty, make publisher_name be the string "NULL".
# [x] c) do a single iteration on the dataset.
# [x] d) !!! remember to close all the filepointers. !!!
# [x] e) make it work for any column name. don't hardcode the string "Publisher".
# [\] f) make the output file format configurable
# [ ] g) permitem ca utilizatorul să specifice output dir.
#        în cazul în care nu este specificat, default este directorul curent.

import sys
import csv
from os import path


CSV_FILENAME_FORMAT = "{fname}_{colname}_{item}{ext}"
NULL_COLUMN_PLACEHOLDER = '__NULL__'


def split_csv_by_column(fname_in, column_name, output_dir="."):
    basename, ext = path.splitext(path.basename(fname_in))

    # Q: câte fișiere vom deschide în with inițial?
    # A: unul singur.
    with open(fname_in) as f:
        bookreader = csv.DictReader(f)

        # Q: ne interesează fieldnames?
        # A: da. dar fără column_name.

        # we need to filter out column_name.
        # method 1. brute force. tried and true.
        fields = []
        for f in bookreader.fieldnames:
            if f == column_name:
                continue
            fields.append(f)
        #print("M1", fields)

        # method 2. filter() with a function.
        # `filter()` returns a virtual object, containing
        # only the elements where the function returned True.
        def filter_for_not_Publisher(name):
            if name == column_name:
                return False
            return True

        fields = tuple(
            filter(filter_for_not_Publisher, bookreader.fieldnames)
        )
        #print("M2", fields)

        # method 2. also filter() with a function,
        # but the function is inline (a lambda).
        fields = tuple(
            filter(
                lambda name: name != column_name,
                bookreader.fieldnames
            )
        )

        # method 3. when we know a list's methods.
        fields = bookreader.fieldnames.copy()
        fields.remove(column_name)
        #print('M3', fields)
        #print('!!', reader.fieldnames)


        # Q: avem de creat (și folosit) o listă necunoscută de fișiere și writere.
        #    cum facem asta?
        # A: folosim un dicționar, unde cheia este nume publisherului, și valoarea
        #    este un DictWriter


        # we initialise a dictionary of csv writers,
        # to deal with each output file
        writers = {}

        # important! each writer will be using a filepointer.
        # unfortunately, the csv.writer / DictWriter interface
        # doesn't allow access to the underlying fp.
        #
        # so we must keep a reference to them,
        # to close them during final cleanup.
        _filepointers = []

        # we must enclose the whole logic in a try / except / finally,
        # to make sure we clean up all open filepointers
        # in case of exception

        try:
            for book in bookreader:
                #publisher = book[column_name]
                # we need to pop the publisher, because we won't write it
                # to the csv 
                value = book.pop(column_name)

                # remember to special case the empty value
                if value == '':
                    value = NULL_COLUMN_PLACEHOLDER

                # did we start working on this value?
                # that is, did we open a file pointer and a csv writer for it?

                try:
                    writer = writers[value]
                except KeyError:
                    # this value is yet unhandled.
                    # we need a new file and writer for it.
                    
                    fname = CSV_FILENAME_FORMAT.format(
                        fname=basename,
                        colname=column_name,
                        item=value,
                        ext=ext,
                    )

                    f = open(path.join(output_dir, fname), 'w', newline='')
                    writer = csv.DictWriter(f, fields)

                    # also remember to write the header
                    writer.writeheader()

                    # and finally, preserve the references
                    _filepointers.append(f)
                    writers[value] = writer

                writer.writerow(book)

        except Exception as e: # <--- capturăm orice fel de excepție
            # we got some error. we should probably do something about it,
            # and not silence it!
            raise e

        finally:
            # we must clean up.
            for fp in _filepointers:
                fp.close()

    # let's report back what was written
    return [
        f.name
        for f in _filepointers
    ]


if __name__ == "__main__":
    # we can handle arguments of the form:
    #   csvin, colname
    # and
    #   csvin, colname, output_dir

    arglength = len(sys.argv)
    if arglength != 3 and arglength != 4:
        # this is an error, we write to stderr
        print(
            "Usage:", sys.argv[0], "<csv in>", "<column name>",
            file=sys.stderr
        )
        # and exit with an error code
        sys.exit(1)

    # write to stdout the list of generated csv files 
    for fname in split_csv_by_column(*sys.argv[1:]):
        print(fname)
