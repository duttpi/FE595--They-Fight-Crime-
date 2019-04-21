
import glob
from textblob import TextBlob
import numpy as np

male = []
female = []
for name in glob.glob('D:/Stevens/595/They Fight Crime/*.txt'):
    if 'female' in name.lower() or 'she' in name.lower() or \
        'women' in name.lower() or 'woman' in name.lower():
        female.append(name)
    else:
        male.append(name)
        
def get_chars(letter, char):
    Lines = []
    senti = []
    for i in range (len(male)):
        with open(male[i]) as file:
            lines=[(line) for line in (file)]
            if len(lines) == 1:
                pass
            else:
                Lines.extend(lines)
                
    for i,item in enumerate(Lines):
        if item[0] != letter:
            Lines[i] = char + item
      
    for item in Lines:
        senti.append(TextBlob(item).sentiment[0])  
        
    return Lines, senti

Lines, polaM = get_chars('H', "He's ")
LinesF, polaF = get_chars('S', "She's ")
Final = Lines + LinesF

Best = Lines[np.argmax(polaM)] + LinesF[np.argmax(polaF)] + 'They fight crime!'
Worst = Lines[np.argmin(polaM)] + LinesF[np.argmin(polaF)] + 'They fight crime!'

adj = []
#ALL = TextBlob(Final)
for i in range(len(Final)):
    adj.extend(Final[i].strip(' ').split(' ')[2:4])
ADJ = ' '.join(adj)


common = {}
for item in ADJ.split(' '):
    if item in common:
        common[item] += 1
    else:
        common[item] = 1
topn = sorted(common.items(), key=lambda x: x[1], reverse = True)
for i in range (10):
    print (topn[i][0], topn[i][1])


