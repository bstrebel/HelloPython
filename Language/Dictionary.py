__author__ = 'bst'

def init(e):
    _entry = e
    print _entry


d = {'entry': { 'value': "Value"} }

#init(d['entry'])



to_import = open("import.py")
exec(to_import)
to_import.close()


