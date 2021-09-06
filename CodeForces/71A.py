""" when a word is too long, that is, having more than 10 characters
it is replaced with an abbreviation.
abbreviation: we write down the first and the last letter of a word and between them we write the number of
letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

so 'localisation' is 'l10n' and 'internationalization' is 'i18n'.
"""

n = int(input())
if 1 <= n <= 100:
    for i in range(1, n+1):
        word = input()
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[len(word) - 1])
        else:
            print(word)
