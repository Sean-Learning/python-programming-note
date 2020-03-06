class A3:
    def __init__(self):
        print("entered A init")
        self.a = "A3"
        print("A inited")
    
    def print_a(self):
        print(self.a)
    def haha(self):
        print("Ahaha")

class B3:
    def __init__(self):
        print("entered B init")
        self.b = "B3"
        print("B inited")
    
    def print_b(self):
        print(self.b)
    def haha(self):
        print("Bhaha")

class C3:
    def __init__(self):
        print("entered C init")
        self.c = "C3"
        print("C inited")
    
    def print_c(self):
        print(self.c)
    def haha(self):
        print("Chaha")

class D3(A3, C3, B3):
    def __init__(self):
        print("entered d inited")
        super().__init__()
        print("super inited")
        super(A3, self).__init__()
        print("A3 self inited")
        
        super(C3, self).__init__()
        #try to replace this line with:
        #super(A3, self).__init__()
        #super(B3, self).__init__()
        #super(D3, self).__init__()
        #and see whats happened
        #super structure here looks like this:
        # D -super-> A -super-> C -super-> B -super-> Nothing


    def haha(self):
        super().haha()
        #super() == super(D3, self)
        super(A3,self).haha()
        # equals to call super in A3
        super().haha()
        super().haha()


d = D3()

d.print_a()
d.print_b()
d.print_c()

d.haha()