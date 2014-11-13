# Takes a string and returns that string in reverse

def reverse(text):
    print ('The length is: %s') %(len(text))
    for i in range(len(text)):
        print text[(len(text)-1)-i],

txt = raw_input('Type the text: ')
reverse(txt)


#def reverse(text):
#    txet = ""
#    for i in range(len(text)):
#        txet += text[(len(text)-1) - i]
#    return txet


