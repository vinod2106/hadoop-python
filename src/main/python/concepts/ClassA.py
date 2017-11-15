class ClassA(object):
    var1 = 1
    var2 = 2

    @classmethod  
    def methodA(self):
        self.var1 = self.var1 + self.var2
        return self.var1
    
class ClassC(ClassA):
    
    def __init__(self):
        ClassA.__init__(self)
        print self.var1
        print self.var2

if __name__ == '__main__':
    obja = ClassA()
    sumw = obja.methodA()
    objc = ClassC()
    print sumw
    
