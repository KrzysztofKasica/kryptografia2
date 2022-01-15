from math import ceil

alfabet = {"a": 1,  "b": 2,  "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

def convert(string):
    convertedString = []
    for letter in string:
        convertedString.append(alfabet[letter])
    return convertedString

def addKey(charArray, key):
    convertedString = []
    for val in charArray:
        val += key
        if val > 26:
            val %= 26
        convertedString.append(val)
    return convertedString

def binaryToInt(charArray):
    convertedString = []
    for val in charArray[2:]:
        convertedString.append(val)
    return convertedString

def finalConversion(charArray, key):
    convertedString = []
    size = len(charArray)
    if size%2 == 0:
        for val in range(ceil(size/2)):
            convertedString.append(int(''.join(binaryToInt(list(bin(charArray[val]))))))
        for val in range(ceil(size/2)):
            convertedString.append(int(''.join(binaryToInt(list(bin(charArray[(int(size/2) + val)]))))))
    else:
        for val in range(ceil(size/2)):
            convertedString.append(int(''.join(binaryToInt(list(bin(charArray[val]))))))
        for val in range(ceil(size/2) - 1):
            convertedString.append(int(''.join(binaryToInt(list(bin(charArray[(ceil(size/2) + val)]))))))
    return convertedString

def addKeyPowered(charArray, key):
    convertedString = []
    size = len(charArray)
    if size%2 == 0:
        for val in range(ceil(size/2)):
            convertedString.append(charArray[val] + key**(size-val))
        for val in range(ceil(size/2)):
            convertedString.append(charArray[(int(size/2) + val)] + key**(int(size/2) + val + 1))
    else:
        for val in range(ceil(size/2)):
            convertedString.append(charArray[val] + key**(size-val))
        for val in range(ceil(size/2) - 1):
            convertedString.append(charArray[(ceil(size/2) + val)] + key**(ceil(size/2) + val + 1))
    return convertedString

def decrypt(charArray, key):
    convertedString = []
    size = len(charArray)
    if size%2 == 0:
        for val in range(ceil(size/2)):
            convertedString.append(charArray[val] - key**(size-val))
        for val in range(ceil(size/2)):
            convertedString.append(charArray[(int(size/2) + val)] - key**(int(size/2) + val + 1))
    else:
        for val in range(ceil(size/2)):
            convertedString.append(charArray[val] - key**(size-val))
        for val in range(ceil(size/2) - 1):
            convertedString.append(charArray[(ceil(size/2) + val)] - key**(ceil(size/2) + val + 1))
    return convertedString

def decryptContinue(charArray):
    convertedString = []
    for val in charArray:
        convertedString.append(int(str(val), 2))
    return convertedString

def decryptFinish(charArray, key):
    convertedString = []
    for val in charArray:
        if val < 7:
            val += 26
        convertedString.append(list(alfabet.keys())[list(alfabet.values()).index(val - key)])
    return convertedString

def printmenu():
    print("1. Zakoduj wiadomosc\n2. Odkoduj wiadomosc")

def inputMyCoded():
    codedWord = []
    newNum = input()
    while newNum != '0':
        try:
            newNum = int(newNum)
        except ValueError:
            print("Kazda litera musi byc liczba calkowita")
            continue
        codedWord.append(newNum)
        newNum = input()
    return codedWord

def menu():
    printmenu()
    x=input("Wybor: ")
    print(chr(27) + "[2J")
    print("Wybor: " + x + "\n")
    if x == '1':
        key = input("Podaj klucz\n")
        try:
            key=int(key)
        except ValueError:
            print("Klucz musi byc liczba calkowita")
            quit()
        text = input("Podaj slowo do zakodowania\n")
        textToConvert = list(text)
        print(textToConvert)
        print(addKey(convert(textToConvert), key))
        print(finalConversion(addKey(convert(textToConvert), key), key))
        result = addKeyPowered(finalConversion(addKey(convert(textToConvert), key), key), key)
        print(*result, sep = " ")
        input("")
    if x == '2':
        key = input("Podaj klucz\n")
        try:
            key=int(key)
        except ValueError:
            print("Klucz musi byc liczba calkowita")
            quit()
        print("Podaj zakodowane slowo liczba po liczbie, wpisz pojedyncze zero kiedy chcesz skonczyc wpisywanie\n")
        text = inputMyCoded()
        print(chr(27) + "[2J")
        print(decrypt(text, key))
        print(decryptContinue(decrypt(text, key)))
        print(decryptFinish(decryptContinue(decrypt(text, key)), key))
        input("")
if __name__ == "__main__":
    menu()