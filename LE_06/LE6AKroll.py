import re


def vowels_and_consonants():
    print("----- Vowels and Consonants -----")
    message = input("Enter a message: ")
    vowels = len(re.findall(r"[aeiouAEIOU]", message))
    consonants = len(re.findall(r"[a-zA-Z]", message))-vowels
    print("\"{}\" contains {} vowels and {} consonants!".format(message,
                                                                vowels,
                                                                consonants))


def t9_number_translator():
    print("----- Alphabetic Telephone Number Translator -----")
    number = input("Enter a 10-digit phone number: (Example: 123-GET-FOOD) ")
    number = re.sub(r"[abcABC]", "2", number)
    number = re.sub(r"[defDEF]", "3", number)
    number = re.sub(r"[ghiGHI]", "4", number)
    number = re.sub(r"[jklJKL]", "5", number)
    number = re.sub(r"[mnoMNO]", "6", number)
    number = re.sub(r"[pqrsPQRS]", "7", number)
    number = re.sub(r"[tuvTUV]", "8", number)
    number = re.sub(r"[wxyzWXYZ]", "9", number)
    print(number)


vowels_and_consonants()
print()
t9_number_translator()
