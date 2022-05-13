#process a sequence of pairs

text = ['The', 'Fulton','Country','Grand', 'Jury','Said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'Country'), ...]

from xml.dom import UserDataHandler
import nltk
nltk.download('inaugural')
from nltk.corpus import brown
fd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories = genre))
genre_word = [(genre, word) 
    for genre in['news', 'romance']
    for word in brown.words(categories = genre)]
    
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])
cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
print(cfd.conditions())
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
(target, fileid[:4])
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
for target in ['america', 'citizen']
if w.lower().startswith(target))

from nltk.corpus import udhr 
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'ibibio_Efik' ]
cfd = nltk.ConfitionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))

cfd.tabulate(conditions = ['English', 'German_Deutsch'], 
        samples = range(10), cumulative = True)

       
