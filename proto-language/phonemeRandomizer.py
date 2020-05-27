import jsons
import json
import csv
from phoneme import Vowel
from typing import List
from random import shuffle
from random import random


with open('defaultVowels.json') as f:
    vowelList = jsons.load(json.load(f), List[Vowel])

# I want to asses each phonem in a random order. This is no relevant in this implementation, 
# but could be in the future
randomOrder = list(range(len(vowelList)))
shuffle(randomOrder)
for i in randomOrder:
    # phonems are more/less likely to be present in the proto-language depending on their prevalence
    if vowelList[i].prevalence < random():
        vowelList[i].isPresent = False

# ensure logical coherence. If a long vowel is present, the short version should also logically exist in the proto-language
# Terrible time complexity is ignored: phonems are at a human scale (small), so theoretical time omplexity can be neglected
# a more advanced implementation would include a phonem table object that keeps track of relationships between phonems, as well as properties like column count
for vowel in vowelList:
    if vowel.isPresent and vowel.length == 'long':
        for i, other in enumerate(vowelList):
            if other.getMouthShape() == vowel.getMouthShape():
                vowelList[i].isPresent = True


with open('proto-phonemes.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    colCount = vowelList[0].getColCount()

    # write headers
    for colTitle in vowelList[0].getColTitles():
        csvWriter.writerow([type(vowelList[0])] + [ getattr(vowelList[j], colTitle) for j in range(colCount) ])
    # write phonem symbols
    for i in range(int(len(vowelList)/colCount)):
        csvWriter.writerow([vowelList[i*colCount].manner] + [ vowel.display() for vowel in vowelList[i*colCount:(i+1)*colCount] ])