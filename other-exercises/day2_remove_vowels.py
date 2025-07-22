# Define a global variable "vowels" as a string containing all vowels (lowercase and uppercase)
# Write a function remove_vowels that receives a string as a parameter and returns the string with vowels removed.

VOWELS = ('aeiouAEIOU')

def remove_vowels(input_str):
    output = ""
    for char in input_str:
        if char not in VOWELS:
            output += char
    return output

text = 'Ala bala,,,,,, ,,,,,,, portocala, si inca ceva'
text_without_vowels = remove_vowels(text)
print(text_without_vowels)
