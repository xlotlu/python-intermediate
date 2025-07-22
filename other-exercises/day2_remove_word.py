# filter_by_agewrite a function that returns an input string, with a given parameter removed

def remove_word(input_txt, word):
    output = ""

    chrs = iter(word)
    seeking = next(chrs)

    for chr in input_txt:
        if chr == seeking:
            try:
                seeking = next(chrs)
            except StopIteration:
                chrs = iter(word)
                seeking = next(chrs)

            # we_are_in_the_middle_of_matching
            continue

        else:
            #if we_are_in_the_middle_of_matching:
            #    1) vezi... că ai păpat niște caractere
            #    2) vezi că trebuie să resetezi pointerul
            output += chr

    return output

print('[result]', remove_word(
    'this is a wordpress full of words with swords',
    'word'
))