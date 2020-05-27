import jsons
from phoneme import Vowel

# This is a short script to generate an initial population of vowel objects. These are then saved to json which can be edited to tweek the prevalence values.

manners = [ 'close', 'near-close', 'close-mid', 'mid', 'open-mid', 'near-open', 'open' ]
places = [ 'front', 'central', 'back' ]
roundedness = [ 'unrounded', 'rounded' ]
lengths = [ 'short', 'long' ]

vowels = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', None, None, None, 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', None, 'ø̞', 'ə', None, None, 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', None, 'ɐ', None, None, None, 'a', 'ɶ', 'ä', None, 'ɑ', 'ɒ']

vowelList = []
i = 0

for manner in manners:
    for place in places:
        for round in roundedness:
            vowelSymbol = vowels[i]
            i += 1
            if vowelSymbol:
                vowel = Vowel(manner, place, round, 'short', vowelSymbol)
                longVowel = Vowel(manner, place, round, 'long', vowelSymbol + 'ː')
            else:
                vowel = Vowel(manner, place, round, 'short')
                longVowel = Vowel(manner, place, round, 'long')

            vowelList.append(vowel)
            vowelList.append(longVowel)


with open('defaultVowel.json', 'w') as f:
    f.write(jsons.dumps(vowelList))
