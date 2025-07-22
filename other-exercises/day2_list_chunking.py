# scrieți o funcție care primind o listă și parametrul nr. întreg `chunk`, returnează o listă de liste de lungime chunk

import math


def chunk_list(lst, chunk):
    max_batch = math.ceil(len(lst) / chunk)

    output = []

    for batch_num in range(max_batch):
        start = batch_num * chunk
        end = (batch_num + 1) * chunk
    
        output.append(lst[start:end])

    return output

cities = ['Arad', 'Berlin', 'Brașov', 'București', 'Budapesta', 'Cluj', 'Hong Kong', 'Iași', 'New York', 'Oradea', 'Suceava', 'Timișoara', 'Târgu Mureș']

city_chunks = chunk_list(cities, 3)

for chunk in city_chunks:
    print("this is chunk #num", chunk)