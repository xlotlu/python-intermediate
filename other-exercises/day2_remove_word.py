# write a function that processes an input string
# and returns it with a specific word removed

def remove_word(input_txt, word):
    """
    removes all occurences of `word` from `input_txt`
    """

    # we instantiate the output as an empty string.
    # we will add to this every character that does not match
    # the first character from `word`

    output = ""

    # we transform `word` into an iterator, so that we can seek
    # on its first character, and when found advance the cursor
    # to the next.
    # (this will help us by not needing to remember
    # the cursor position.)

    chrs = iter(word)
    seeking = next(chrs)

    # this will be a buffer to preserve partially matched strings,
    # in order to glue them back in case of a partial match.
    #
    # it will also help us know if we are currently in the process of matching.
    current_match = ""

    # we iterate through the input character by character,
    # looking for the current match
    for chr in input_txt:
        if chr == seeking:
            current_match += chr

            # if we found the current character in `word`,
            # try to advance the cursor to the next
            try:
                seeking = next(chrs)
            except StopIteration:
                # this means we found all characters in `word`.
                # this is now a full match, so we reset everything
                chrs = iter(word)
                seeking = next(chrs)
                current_match = ""

        else:
            # this is not a match.

            if current_match:
                # if we have a partial previous match,
                # we need to glue back the lost characters

                output += current_match

                # and reset everything
                chrs = iter(word)
                seeking = next(chrs)
                current_match = ""

            output += chr

    return output

#print('[result]', remove_word(
#    'this is a wordpress full of words with swords',
#    'word'
#)