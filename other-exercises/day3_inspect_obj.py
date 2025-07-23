# write a function `inspect(obj)` that prints the names
# of all attributes of `obj` that do not start
# with an underscore.
#
# they will be printed on a single line.


def inspect(obj):
    for attr in dir(obj):
        if not attr.startswith('_'):
            print(attr, end=' ')



def inspect2(obj):
    attrs = []

    for attr in dir(obj):
        if not attr.startswith('_'):
            attrs.append(attr)

    return attrs
