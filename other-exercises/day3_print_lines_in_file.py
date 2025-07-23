# write a function that receives a filename as argument,
# and prints all the lines in the file
# prepended by the line number, in the format
# number: content

def print_lines(fname):
    for idx, line in enumerate(open(fname)):
        print(idx, line, sep=': ', end='')

print_lines('/tmp/tales.txt')
