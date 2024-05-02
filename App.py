import random

import pandas as pd

VerbList = pd.read_csv('Verbs 2.csv')

tenses = ["perfect", "imperfect", "present", "future", "pluperfect"]
perfectEndings = ["i", "isti", "it", "imus", "istis", "erunt"]
imperfectEndings = ["bam", "bas", "bat", "bamus", "batis", "bant"]
presentEndings = ["o", "s", "t", "mus", "tis", "nt"]
future12Endings = ["bo", "bis", "bit", "bimus", "bitis", "bunt"]
future34Endings = ["am", "es", "et", "emus", "etis", "ent"]
pluperfectEndings = ["eram", "eras", "erat", "eramus", "eratis", "erant"]

ranVerbRow = VerbList.sample()
ranTense = random.choice(tenses)
print(ranVerbRow)
print(ranTense)
def choseEnding(ranVerbRow):
    if ranTense == "perfect":
        unchangedVerb = ranVerbRow.iloc[0,2]
        return random.choice(perfectEndings)
    elif ranTense == "imperfect":
        unchangedVerb = (ranVerbRow.iloc[0,1])[:-2]
        return random.choice(imperfectEndings)
    elif ranTense == "present":
        
        return random.choice(presentEndings)
    elif ranTense == 'pluperfect':
        return random.choice(pluperfectEndings)
    elif ranTense == 'future':
        if "verb 1" or "verb 2" in ranVerbRow:
            return random.choice(future12Endings)
        elif "verb 3" or "verb 4" in ranVerbRow:
            return random.choice(future34Endings)


chosenEnding = choseEnding()
print (chosenEnding)

print(ranVerbRow.iloc[0,2])
