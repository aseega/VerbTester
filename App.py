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
if ranTense == "perfect":
    unchangedVerb = ranVerbRow.iloc[0,2]
    ending = random.choice(perfectEndings)
    finalVerb = unchangedVerb + ending
elif ranTense == "imperfect":
    unchangedVerb = (ranVerbRow.iloc[0,1])[:-2]
    ending = random.choice(imperfectEndings)
    finalVerb = unchangedVerb + ending
elif ranTense == "present":
    ending = random.choice(presentEndings)
    if "verb 1" in ranVerbRow:
        unchangedVerb = ranVerbRow.iloc[0,0][:-1]
        print(unchangedVerb)
        if ending == "o":
            finalVerb = unchangedVerb + "o"
        else:
            finalVerb = unchangedVerb + "a" + ending
    elif "verb 2" in ranVerbRow:
        unchangedVerb = ranVerbRow.iloc[0,0][:-1]
        print(unchangedVerb)
        if ending == "o":
            finalVerb = unchangedVerb + "o"
        else:
            finalVerb = unchangedVerb + "e" + ending

    elif "verb 3" in ranVerbRow:
        unchangedVerb = ranVerbRow.iloc[0,0][:-1]
        if ending == "o":
            finalVerb = unchangedVerb + "o"
        elif ending == "nt":
            finalVerb = unchangedVerb + "unt"
        else:
            finalVerb = unchangedVerb + "i" + ending

    elif "verb 4" in ranVerbRow:
        unchangedVerb = ranVerbRow.iloc[0,0][:-1]
        if ending == "nt":
            finalVerb = unchangedVerb + "iunt"
        else:
            finalVerb = unchangedVerb + 'i' + ending

    
    ending = random.choice(presentEndings)
elif ranTense == 'pluperfect':
    ending = random.choice(pluperfectEndings)
    unchangedVerb = ranVerbRow.iloc[0,2]
    finalVerb = unchangedVerb + ending

elif ranTense == 'future':
    if "verb 1" or "verb 2" in ranVerbRow:
        ending = random.choice(future12Endings)
        unchangedVerb = (ranVerbRow.iloc[0,1])[:-3]
        finalVerb = unchangedVerb + ending

        
    elif "verb 3" or "verb 4" in ranVerbRow:
        ending = random.choice(future34Endings)
        unchangedVerb = (ranVerbRow.iloc[0,1])[:-2]
        finalVerb = unchangedVerb + ending


print(finalVerb)
