"""
given a list of people and their ages,
filter the people that are between min and max.

create a list of accepted people, sorted by age
"""

MIN_AGE = 25
MAX_AGE = 45


people = (
    ('Gi Gel', 32),
    ('Ionu Tz', 44),
    ('Ionuț C', 27),
    ('The Other Guy', 37),
    ('Silvia', 24),
    ('Ze Olde Guy', 64),
    ('And Another', 26),
)

accepted = []

for person in people:
    name = person[0]
    age = person[1]

    #print(age, ":", name)

    if age >= MIN_AGE and age <= MAX_AGE:
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


for p in accepted:
    print(p)

