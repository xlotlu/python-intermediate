# given a file of the format of people.txt
#
# name[tab]age[tab]is_customer
# name 1[tab]age 1[tab]true/false
#
# a) write a function processing the file and returning
# a list of tuples
#
# b) write a function processing the file and returning
# a list of dictionaries

import warnings

def load_people_to_tuples(file_in):
    # we instantiate our output variable
    people_list = []

    # we open the file
    with open(file_in) as f:
        # we iterate over the file pointer, line by line

        # but the first line is the header, we need to skip it
        header = next(f)
        #print('header is:', header)

        for idx, line in enumerate(f, start=2):
            # warning: line may or may not end with a "\n"
            line = line.replace("\n", "")
            
            if line == "":
                continue

            try:
                name, age, is_customer = line.split("\t")
            except ValueError:
                print('malformed input data on line %s: "%s"' % (idx, line))
                continue
            age = int(age)

            is_customer = is_customer.lower()
            if is_customer == 'true':
                is_customer = True
            elif is_customer == 'false':
                is_customer = False
            else:
                # alert!
                print('is_customer: malformed / unknown data: ' + is_customer)
            
            people_list.append(
                (name, age, is_customer)
            )

    return people_list

def load_people_to_dictionaries(file_in):
    pass

print(
load_people_to_tuples('people.txt')
)