# Totals the number of points in a scrabble word

def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    total = 0
    for i in word:
        if i.lower() in score:
            total += score[i.lower()]
    return total

wrd = raw_input('Type the word: ')
print ('Your score is %d') %(scrabble_score(wrd))
