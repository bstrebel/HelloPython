__author__ = 'BST'

class BaseClass():

    def __init__(self, data):
        self._data = data

    def run(self):
        from sub import SubClass
        sc = SubClass(self._data)
        sc.show()
        self.show()

    def show(self):
        print 'base', self._data


def main():

    data = { 'key':'value'}
    BaseClass(data).run()



if __name__ == '__main__': main()
