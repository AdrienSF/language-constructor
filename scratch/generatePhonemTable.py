import json
from tabulate import tabulate
from functools import reduce
# load full phonem table from json file
with open('vowelDict.json') as f:
    vowelDict = json.load(f)

def unpack(nestedDict: dict):
    # base case: dict does not contain dicts
    if not isinstance(nestedDict[next(iter(nestedDict))], dict):
        return [ nestedDict[key] for key in nestedDict ]
    # recursive case: nestedDict is in fact a nested dict
    else:
        items = []
        for key in nestedDict:
            items += unpack(nestedDict[key])
        return items

def getKeys(nestedDict: dict):
    if isinstance(nestedDict, dict):
        keys = [ key for key in nestedDict ]
        nestedKeys = getKeys(nestedDict[keys[0]])
        if nestedKeys:
            return [ keys ] + nestedKeys
        else:
            return [ keys ]

def getHeader(headerKeys: list):
    # get the total number of columns/titles in the header
    titleCount = reduce((lambda x, y: x * y), [len(keyList) for keyList in headerKeys] )
    header = []
    for i in range(titleCount):
        title = []
        for j in range(len(headerKeys)):
            # add the titles in the right order
            titleSubsetProduct = reduce((lambda x, y: x * y), [len(keyList) for keyList in headerKeys[:j+1]] )
            title.append(headerKeys[j][ int(i*titleSubsetProduct/titleCount) % len(headerKeys[j])])
        header.append('\n'.join(title))
    return header




vowelList = unpack(vowelDict)
keyList = getKeys(vowelDict)
header = getHeader(keyList[1:])
# print(vowelList)
# print()
# print(keyList)
# print()
# print(header)
firstColumn = keyList[0]
vowelMatrix = [ [firstColumn[int(i/len(header))]] + vowelList[i:i+len(header)] for i in range(0, len(vowelList), len(header))]
# print(vowelMatrix)

# for key in vowelDict:
#     row = vowelDict[key]
#     rowList = []
#     for key in row:
#         col = row[key]
#         for key in col:
#             type = col[key]
#             for key in type:
#                 symbol = type[key]
#                 rowList.append(symbol)
#     vowelList.append(rowList)


print(tabulate(vowelMatrix, headers=header, stralign='center'))
