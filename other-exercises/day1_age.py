"""
un script care verifică vârsta utilizatorului
sunt acceptați doar utilizatori între minim și maxim.

dacă are vârsta perfectă primește mesaj special.
"""

MIN_AGE = 25
MAX_AGE = 45

PERFECT_AGE = 32


age = input("Ce vârstă ai? ")
age = int(age)

if age < MIN_AGE:
    # respins 1
    print("prea tânăr")

elif age > MAX_AGE:
    # respins 2
    print("prea în vârstă")

elif age == PERFECT_AGE:
    # mesaj perfect
    print("ideal")

else:
    # acum suntem ok
    print("ok")

