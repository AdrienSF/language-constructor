# a more extensive implementation (use ordered enums for manner place...) was attempted in the scratch folder, 
# but this implementation is sufficient to select random phonemes
class Phoneme:
    def __init__(self, manner: str, place: str, symbol=None, prevalence=0):
        self.manner = manner
        self.place = place
        self.symbol = symbol
        self.prevalence = prevalence
        self.isPresent = bool(symbol)

    def __str__(self):
        return str(self.symbol)

    def display(self):
        if self.isPresent:
            return self.symbol
        else:
            return ''





class Vowel(Phonem):
    def __init__(self, manner: str, place: str, roundedness: str, length: str, symbol=None, prevalence=0):
        super().__init__(manner, place, symbol, prevalence)
        self.roundedness = roundedness
        self.length = length

    def getColTitles(self):
        return ['place', 'roundedness', 'length']

    # shameless, un-agile hack fix. There should be a table object to do this instead
    def getColCount(self):
        return 12

    def getMouthShape(self):
        return {
            'manner': self.manner,
            'place': self.place,
            'roundedness': self.roundedness
        }
