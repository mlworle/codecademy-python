# A function that takes Text and Word. Replaces "*"s for Word in Text.
# Assumes all alphabetical characters no !?@#$% etc.

def censor(text, word):
    temp = text.split()
    phrase = []
    for i in temp:
        if i == word:
            i = "*" * len(word)
            phrase.append(i)
        else:
            phrase.append(i)
    return " ".join(phrase)

txt = raw_input("What is the phrase? ")
wrd = raw_input("What is the word? ")
print("This is the new phrase:   %s") %(censor(txt, wrd))
