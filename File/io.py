import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['adsd','dwedwe','ewdwedwe']
shelfFile.close()

data = shelve.open('mydata')
print(data['cats'])

print(list(data.keys()))
print(list(data.values()))
