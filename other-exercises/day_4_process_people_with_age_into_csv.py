# given a file of the format of ages.txt
#
# name[tab]age
#
# write a function
# `process_people_to_csv(fname_in, fname_out)`
# that writes into `fname_out` in csv format the following:
#
# header (column names)
# row1, row2, etc...
# 
# and finally a footer containing the following cells:
# - the string "rowcount"
# - the number of people
# - the string "average"
# - the average age
# - the string "min"
# - the minimum age
# - the string "max"
# - the maximum age

import csv
import math
from day_4_process_people_with_age import process_people 

def process_people_to_csv(fname_in, fname_out):
    people = process_people(fname_in)

    count = 0
    age_min = math.inf
    age_max = 0
    age_sum = 0

    with open(fname_out, 'w') as f:
        writer = csv.DictWriter(f, ('name', 'age'))
        writer.writeheader()

        # write each row
        for d in people:
            writer.writerow(d)

            count += 1
            age_max = max(age_max, d['age'])
            age_min = min(age_min, d['age'])
            age_sum += d['age']

        # write footer
        footwriter = csv.writer(f)
        footwriter.writerow([
            "rowcount", count,
            "average", age_sum / count,
            "min", age_min,
            "max", age_max,
        ])