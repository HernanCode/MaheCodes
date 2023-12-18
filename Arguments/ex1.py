# Fes un programa que accepta 1 argument per la línia de comandes i, 
# si està format per lletres a-z o A-Z, mostra per pantalla quantes vocals té.

import sys

def vowel_count(word):
    vowels = sum([1 for letter in word if letter.lower() in "aeiou"])
    return vowels

def main():
    word = sys.argv[1]
    if __name__ == "__main__":
        num_vowels = vowel_count(word)
        print(num_vowels)
if __name__ == "__main__":
    main()
