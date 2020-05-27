import json
import jsons
from phonem import Vowel
from phonem import Manner
from phonem import Place
from phonem import Roundedness
from phonem import Length
import csv
from parsing import PhonemTableParser



manners = [ Manner.close, Manner.near_close, Manner.close_mid, Manner.mid, Manner.open_mid, Manner.near_open, Manner.open ]
places = [ Place.front, Place.central, Place.back ]
roundedness = [ Roundedness.unrounded, Roundedness.rounded ]
lengths = [ Length.short, Length.long ]

vowels = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', None, None, None, 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', None, 'ø̞', 'ə', None, None, 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', None, 'ɐ', None, None, None, 'a', 'ɶ', 'ä', None, 'ɑ', 'ɒ']

# with open('vowelTable.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     line1 = ['']
#     line2 = []
#     line3 = []
#     for place in places:
#         line1 += [place._name_,'','','','','']
#     for round in roundedness:
#         line2 += [round._name_,'','','']
#     line2 = [''] + line2 + line2 + line2
#     linePart = []
#     for length in lengths:
#         linePart += [length._name_, 'prevalence' ]
#     for i in range(12):
#         line3 += linePart
#     line3 = [''] + line3


#     writer.writerow(line1)
#     writer.writerow(line2)
#     writer.writerow(line3)

#     lines = []
#     for vowel in vowels:


#     for i in range(len(manners)):
#         writer.writerow( [manners[i]._name_] + lines[i:i+24] )
    

# exit(0)

symbolDict = {}
vowelDict = {}
i = 0

for manner in manners:
    vowelDict[manner._name_] = {}
    for place in places:
        vowelDict[manner._name_][place._name_] = {}
        for round in roundedness:
            vowelSymbol = vowels[i]
            i += 1
            if vowelSymbol:
                vowel = Vowel(manner, place, round, Length.short, vowelSymbol)
                longVowel = Vowel(manner, place, round, Length.long, vowelSymbol + 'ː')
            else:
                vowel = Vowel(manner, place, round, Length.short)
                longVowel = Vowel(manner, place, round, Length.long)
            # print('should be: ' + str(manner))
            # print('is: ' + str(vowel.manner))
            
            vowelDict[manner._name_][place._name_][round._name_] = {
                Length.short._name_: vowel,
                Length.long._name_: longVowel
            }

            # print(longVowel.__repr__)
            # print(vowel.__repr__)

            
parser = PhonemTableParser()
vowelList = parser.unpack(vowelDict)
print(vowelList)
parser.serialize('vowelTable.csv', vowelList)
# serialized = jsons.dump(vowelDict, verbose=True)
# print(serialized)
# print()
# print()
# print(jsons.load(serialized, Vowel))

# with open("vowelDict.json", 'w') as f:
#     f.write(json.dumps(vowelDict))
