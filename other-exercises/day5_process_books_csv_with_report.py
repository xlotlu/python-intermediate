#!/usr/bin/env python

# using the dataset under `books.csv`:
# [x] - read the csv
# [x] - write out separate files for each publisher,
#       named "books_Publisher_<publisher_name>.csv".
# [ ] - write out a `report.json` file, containing
#       book_count, author_count, publisher_count, genre_count,
#
# extra-requirements:
# [x] a) skip the "Publisher" column in the output.
# [x] b) if the Publisher is empty, make publisher_name be the string "NULL".
# [x] c) do a single iteration on the dataset.
# [x] d) !!! remember to close all the filepointers. !!!
# [x] e) make it work for any column name. don't hardcode the string "Publisher".
# [\] f) make the output file format configurable
# [x] g) permitem ca utilizatorul să specifice output dir.
#        în cazul în care nu este specificat, default este directorul curent.

import sys
import csv
import json
from os import path


CSV_FILENAME_FORMAT = "{fname}_{colname}_{item}{ext}"
NULL_COLUMN_PLACEHOLDER = '__NULL__'
REPORT_FILENAME = 'report.json'


def split_csv_by_column(fname_in, column_name,
                        output_dir=".",
                        report_columns=None,
                        ):
    basename, ext = path.splitext(path.basename(fname_in))

    if report_columns is None:
        # nu scriem raport
        pass
    else:
        report_columns = report_columns.split(',')

    report = {
        col: {}
        for col in report_columns
    }

    with open(fname_in) as f:
        bookreader = csv.DictReader(f)

        # we need to filter out column_name.
        fields = bookreader.fieldnames.copy()
        fields.remove(column_name)

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
                # we prepare the report before anything,
                # because the column we're working on will disappear later
                for col in report_columns:
                    subreport = report[col]
                    r_key = book[col]
                    subreport[r_key] = subreport.get(r_key, 0) + 1

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

            if report_columns:
                with open(path.join(output_dir, REPORT_FILENAME), 'w') as repf:
                    json.dump(report, repf, indent=2)

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
    if 3 <= arglength <= 5:
        # all ok.
        # write to stdout the list of generated csv files 
        for fname in split_csv_by_column(*sys.argv[1:]):
            print(fname)
    else:
        # this is an error, we write to stderr
        print(
            "Usage:", sys.argv[0], "<csv in>", "<column name>",
            file=sys.stderr
        )
        # and exit with an error code
        sys.exit(1)
