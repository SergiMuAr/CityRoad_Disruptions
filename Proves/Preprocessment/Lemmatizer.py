
class myLemmatizer:
    def __init__(self):
        with open('lemmatization-ca.txt', 'rb') as f:
            data = f.read().decode('utf8').replace(u'\r', u'').split(u'\n')
            data = [a.split(u'\t') for a in data]
            
            self.lemmaDict = { a[1]:a[0] for a in data if len(a)>1 }
            self.lemmaDict.update( { a:a for a in set(self.lemmaDict.values()) } )

    def lemmatize(self, word):
        return self.lemmaDict.get(word, word + u'*')

    def test(self):
        for a in [ u'sortiries', u'usuaris', u'cantimplores']:
            print(self.lemmatize(a))

