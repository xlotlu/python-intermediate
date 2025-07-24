# scrieți o funcție `countlines(fname)` ce returnează
# numărul de linii dintr-un fișier.
#
# NU folosiți f.readlines().
# faceți funcția să fie cât mai eficientă posibil
# d.p.d.v. al alocării memoriei.


def countlines(fname):
    with open(fname) as f:
        # we will read only some characters at a time
        chunk = 20

        content = f.read(chunk)
        count = 1 if content else 0

        while content:
            # how many \n are in content?
            count += content.count("\n")

            content = f.read(chunk)

    return count

print(countlines('/tmp/ok.txt'))
