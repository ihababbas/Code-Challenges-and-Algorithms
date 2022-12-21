from collections import Counter

def firstRepeat(string):
    '''
     :type string: string
     :rtype: string
     '''
    words = set()
    for word in string.split():
        if word in words:
            return word
        else:
            words.add(word)
    return 'No Repetition'
    
    
ex1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
print(firstRepeat(ex1))
ex2 = "I am learning programming at ASAC."
print(firstRepeat(ex2))