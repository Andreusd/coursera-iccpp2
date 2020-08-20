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
        
        
