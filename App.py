from pandas import pd
import random

VerbList = pd.read_csv('/Verbs.csv')

tenses = ["perfect", "imperfect", "present", "future", "pluperfect"]
perfectEndings = ["i", "isti", "it", "imus", "istis", "erunt"]
imperfectEndings = ["bam", "bas", "bat", "bamus", "batis", "bant"]
presentEndings = ["o", "s", "t", "mus", "tis", "nt"]
future12Endings = ["bo", "bis", "bit", "bimus", "bitis", "bunt"]
future34Endings = ["am", "es", "et", "emus", "etis", "ent"]
pluperfectEndings = ["eram", "eras", "erat", "eramus", "eratis", "erant"]

ranVerb = csvfile.sample()
ranTense = random.choice(tenses)
print(ranVerb)
print(ranTense)
