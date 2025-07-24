# given a file of the format of ages.txt
#
# name[tab]age
#
# write a function that reads the file
# and returns a list of dictionaries 
# of the form {'name': ..., 'age': ... }

def process_people(fname):
    list_people = []
    with open(fname) as file_in:
        for line in file_in:
            name, age = line[:-1].split('\t')
            age = int(age)
            # and returns a list of dictionaries 
            # of the form {'name': ..., 'age': ... }
            list_people.append({
                'name': name,
                'age': age,
            })
    return list_people
    


data = process_people('ages.txt') # relative path
for item in data:
    print(item)