import numpy as np

def bitap(haystack, needle, maxErrors=3):
    haystackLen = len(haystack)
    needleLen = len(needle)

    def _generateAlphabet(needle, haystack):
        alphabet = {}
        for letter in haystack:
            if letter not in alphabet:
                letterPositionInNeedle = 0
                for symbol in needle:
                    letterPositionInNeedle = letterPositionInNeedle << 1
                    letterPositionInNeedle |= int(letter != symbol)
                alphabet[letter] = letterPositionInNeedle
        return alphabet

    alphabet = _generateAlphabet(needle, haystack)

    table = []
    emptyColumn = (2 << (needleLen - 1)) - 1

    underground = [emptyColumn for i in range(haystackLen + 1)]
    
    table.append(underground)
    k = 1
    table.append([emptyColumn])
    for columnNum in range(1, haystackLen + 1):
        prevColumn = (table[k][columnNum - 1]) >> 1
        letterPattern = alphabet[haystack[columnNum - 1]]
        curColumn = prevColumn | letterPattern
        table[k].append(curColumn)
        if (curColumn & 0x1) == 0:
            return k - 1
    for k in range(2, maxErrors + 2):
        table.append([emptyColumn])

        for columnNum in range(1, haystackLen + 1):
            prevColumn = (table[k][columnNum - 1]) >> 1
            letterPattern = alphabet[haystack[columnNum - 1]]
            curColumn = prevColumn | letterPattern
            
            insertColumn = curColumn & (table[k - 1][columnNum - 1])
            deleteColumn = curColumn & (table[k - 1][columnNum] >> 1)
            replaceColumn = curColumn & (table[k - 1][columnNum - 1] >> 1)
            resColumn = insertColumn & deleteColumn & replaceColumn
            
            table[k].append(resColumn)
            if (resColumn & 0x1) == 0:
                return k - 1
    return 1000000

if __name__=='__main__':
    word_1 = 'лызина'
    word_2 = 'лыткина'
    print(f'Расстояние левенштейна между словами \'{word_1}\' и \'{word_2}\' равно {bitap(word_1, word_2)}\n')