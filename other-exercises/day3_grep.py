# write a function `grep(match, fname)` which,
# given a string and a filename, returns a list
# of all the lines in the file that match the string.


def grep(match, fname):
    out = []

    for line in open(fname):
        if match in line:
            out.append(line)

    return out
