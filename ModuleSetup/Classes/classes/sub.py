__author__ = 'BST'

from base import BaseClass

class SubClass(BaseClass):

    def __init__(self, data):
        self._data = data
        self._data['sub init'] ='value'
        BaseClass.__init__(self, self._data)

    def show(self):
        print 'SubClass', self._data

def main():
    data = {'sub main': 'value'}
    sub = SubClass(data)
    sub.show()


if __name__ == '__main__': main()
