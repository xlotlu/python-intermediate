# using the dataset under `books.csv`:
# - read the csv
# - create an aggreggate for the `Genre` column, of the form
#   genre_aggreggate = {
#       genre: count,
#       ...
#   }
# - write out a json file of the form {
#      "genres": {
#           genre: count,
#           ...
#      }
#   }


"""
1. open input csv file
2. open output json file
3. dataset = csv.DictReader()
4. iterate over the dataset
5. calculate aggreggate
6. write to json
"""

