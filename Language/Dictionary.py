__author__ = 'bst'

myDict = {'key1': 'value1',
          'key2': 'value2'}

myDict.setdefault('scraper', {})

for k in myDict.keys():
    print(k)

if 'key1' in myDict:
    print("Found!")

for k, v in myDict.items():
    print(k, v)

print('[myDict]')
for d in myDict:
    print(d)





def init(e):
    _entry = e
    print _entry


d = {'entry': { 'value': "Value"} }

#init(d['entry'])



to_import = open("import.py")
exec(to_import)
to_import.close()


