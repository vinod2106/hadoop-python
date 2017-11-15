'''
Created on 10 Nov 2017

@author: vinsharm
'''
class ClassA(object):
    var1 = 0
    var2 = 0
    def __init__(self):
        self.var1 = 1
        self.var2 = 2

    def methodA(self):
        self.var1 = self.var1 + self.var2
        return self.var1



class ClassB(ClassA):
    def __init__(self):
        ClassA.__init__(self)
        print self.var1
        print self.var2

if __name__ == '__main__':
    object1 = ClassA()
    sumw = object1.methodA()
    object2 = ClassB()
    print sumw
