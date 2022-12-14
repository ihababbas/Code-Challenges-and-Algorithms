from collections import Counter

def firstRepeat(string):
    '''
     :type string: string
     :rtype: string
    '''
    words = string.split(" ")
    dict = Counter(words)
    
    for key in words:
        if dict[key] > 1:
            return key
    else:
        return "No Repetition"
    
    
ex1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
print(firstRepeat(ex1))
ex2 = "I am learning programming at ASAC."
print(firstRepeat(ex2))