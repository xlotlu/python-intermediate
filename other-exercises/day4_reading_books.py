# using the dataset under `books.csv`:
# - read the csv
# - filter the data on `Genre` = "mathematics" and "computer_science"
# - create two other CSV files: mathematics_books.csv and computer_science_books.csv,
#   containing only books in each genre

import csv

with open('docs/books.csv') as f, \
     open('mathematics_books.csv', 'w', newline='') as mbf, \
     open('computer_science_books.csv', 'w', newline='') as cbf:

    books = csv.DictReader(f)
    m_books = csv.DictWriter(mbf, books.fieldnames)
    c_books = csv.DictWriter(cbf, books.fieldnames)

    m_books.writeheader()
    c_books.writeheader()

    for book in books:
        if book['Genre'] == 'computer_science':
            c_books.writerow(book)
        elif book['Genre'] == 'mathematics':
            m_books.writerow(book)
