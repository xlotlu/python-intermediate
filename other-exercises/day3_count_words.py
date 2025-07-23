# write a function `count_words(text)` that counts the occurances
# of each word inside a string, returning a dictionary
# of the form { 'word': count }

nonword = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~'

def count_words(text):
    # inițializăm dicționar de output
    out = {}

    # curățăm textul de input de caractere care nu pot apărea într-un cuvânt
    # TODO: make this efficient using text.translate()
    for c in nonword:
        text = text.replace(c, '')

    words = text.lower().split()

    for word in words:
        out[word] = out.get(word, 0) + 1

    return out



print(
    count_words(
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."
    )
)