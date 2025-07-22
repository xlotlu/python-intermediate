"""
write a function `filter_by_age(people, min_age, max_age)`
that returns people filtered and sorted by age.

people is a list of the form [('Name 1', age1), ('Name 2', age2)... ]
"""

MIN_AGE = 25
MAX_AGE = 45

def filter_by_age(people, min_age=MIN_AGE, max_age=MAX_AGE):
    accepted = []

    for person in people:
        name = person[0]
        age = person[1]

        #print(age, ":", name)

        if age >= min_age and age <= max_age:
            # print(name, 'are', age, 'ani')

            position = 0
            for acc in accepted:
                if age < acc['age']:
                    break

                position += 1

            accepted.insert(position, {
                'age': age,
                'name': name,
            })

    return accepted



people = (
    ('Gi Gel', 32),
    ('Ionu Tz', 44),
    ('Ionuț C', 27),
    ('The Other Guy', 37),
    ('Silvia', 24),
    ('Ze Olde Guy', 64),
    ('And Another', 26),
)


for p in filter_by_age(people, 20, 30):
    print(p)

