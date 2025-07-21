"""
given a list of people and their ages,
filter the people that are between min and max.

create a list of accepted people,
and a list of rejected people.
"""

MIN_AGE = 25
MAX_AGE = 45


people = (
    ('Ionu Tz', 22),
    ('Ionuț C', 32),
    ('Silvia', 24),
    ('Ze Olde Guy', 64),
    ('The Other Guy', 37),
)

accepted = []
rejected = []

for person in people:
    name = person[0]
    age = person[1]

    print(age, ":", name)

    if age >= MIN_AGE and age <= MAX_AGE:
        accepted.append(name)
    else:
        rejected.append(name)

print("accepted:", accepted)
print("rejected:", rejected)

