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

from day_4_process_people_with_age import process_people 

def process_people_to_csv(fname_in, fname_out):
    rows = process_people(fname_in)

