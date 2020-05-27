import csv
from functools import reduce
from phonem import Vowel
from phonem import Manner
from phonem import Place
from phonem import Roundedness
from phonem import Length
import jsons
import json

class PhonemTableParser:
    def serialize(self, csvFileName: str, phonemList: list):
        rowCount = 7
        items = phonemList
        colCount = int(len(items)/rowCount)
        header = self.getHeader(phonemList[:colCount])

        with open(csvFileName, mode='w') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # for header in headers:
            #     csvWriter.writerow(header)
            csvWriter.writerow(header)
            for i in range(rowCount):
                row = []
                for item in items[i*colCount:(i+1)*colCount]:
                    print(item)
                    row += [ str(item), item.prevalence ]
                row = [ item.manner._name_ ] + row
                csvWriter.writerow(row)


    def deserialize(self, csvFileName: str):
        phonemList = []
        with open(csvFileName, newline='') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
            first = next(csvReader)
            row1 = [ first[i] for i in range(1, len(first), 2) ]

            print(row1)
            header = [first[0]] + [ json.loads(title) for title in row1[1:] ]
            i = 1
            for row in csvReader:
                i += 1
                for j in range(1, len(row), 2):
                    # pass
                    phonem = Vowel(Manner[row[0]], Place[header[j]['place']], Roundedness[header[j]['roundedness']], Length[header[j]['length']], row[j], row[j+1])
                    # phonemList.append(phonem)
                    print(phonem.__repr__)

        # return phonemList



    def unpack(self, nestedDict: dict):
        # base case: dict does not contain dicts
        if not isinstance(nestedDict[next(iter(nestedDict))], dict):
            return [ nestedDict[key] for key in nestedDict ]
        # recursive case: nestedDict is in fact a nested dict
        else:
            items = []
            for key in nestedDict:
                items += self.unpack(nestedDict[key])
            return items

    def getKeys(self, nestedDict: dict):
        if isinstance(nestedDict, dict):
            keys = [ key for key in nestedDict ]
            nestedKeys = self.getKeys(nestedDict[keys[0]])
            if nestedKeys:
                return [ keys ] + nestedKeys
            else:
                return [ keys ]

    def getHeader(self, aRow: list):
        header = []
        for phonem in aRow:
            phonem.prevalence = None
            phonem.symbol = None
            header.append(phonem.getTitle())
            header.append('prevalence')

        return [str(type(aRow[0]))] + header
        
        