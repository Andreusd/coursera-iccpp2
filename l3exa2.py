class Triangulo():
    def __init__(self,lado_a, lado_b, lado_c):
        self.a=lado_a
        self.b=lado_b
        self.c=lado_c
    def perimetro(self):
        return(self.a+self.b+self.c)
    def tipo_lado(self):
        if(self.a==self.b and self.b==self.c):
            return("equilátero")
        elif(self.a==self.b or self.b==self.c or self.a==self.c):
            return("isósceles")
        else:
            return("escaleno")
    def retangulo(self):
        if(self.a**2==self.b**2+self.c**2):
            return True
        if(self.b**2==self.c**2+self.a**2):
            return True
        if(self.c**2==self.a**2+self.b**2):
            return True
        return False
    def semelhantes(self, other):
        l1=sorted([self.a,self.b,self.c])
        l2=sorted([other.a,other.b,other.c])
        if(l1[0]%l2[0]==0 and l1[1]%l2[1]==0 and l1[2]%l2[2]==0):
            return(True)
        if(l2[0]%l1[0]==0 and l2[1]%l1[1]==0 and l2[2]%l1[2]==0):
            return(True)
        return(False)
            
