class vector2D():
    _count = 0
    def __init__(self,absc = 0,ord = 0):  #absc=the abscissa orn=ordinate of a vector (x,y).
        self._absc = absc
        self._ord =  ord 

#THE GETTERS
    def getabsc (self):
        return self._absc
    
    def getord (self):
        return self._ord

#THE SETTERS
    def setabsc(self,absc):
        self._absc = absc

    def setord(self,ord):
        self._ord = ord

#THE METHODES
    def TOSTRING(self):
        print(f" the abscissa ={self.getabsc()}")
        print(f" the ordinate ={self.getord()}")

    def equals(self,vector2): #the comparison between two vectors.
        #the first vector.
        absc1 = self.getabsc()
        ord1 = self.getord()
        #the second vector.
        absc2 = vector2.getabsc()
        ord2 = vector2.getord()
        if (absc1 == absc2) and (ord1 == ord2) :
            return True
        else:
            return False
        
    def norm(self): #the vector norm.
        print("the norm of this vector :", ((self._absc)**2+(self._ord)**2)**0.5)




class vector3D(vector2D): #the child class.
    def __init__(self,absc,ord, hei ): #hei = height of the vector (z).
        super().__init__(absc,ord)
        self._hei = hei

#THE GETTER
    def gethei(self):
        return self._hei
    
#THE SETTER
    def sethei(self,hei):
        self._hei = hei 
    
#THE METHODES
    def TOSTRING(self):
        print(f" the abscissa ={self.getabsc()}")
        print(f" the ordinate ={self.getord()}")    
        print(f" the height ={self.gethei()}")  


    def equals(self,vector3): #the comparison between two vectors.
        #the first vector.
        absc1 = self.getabsc()
        ord1 = self.getord()
        hei1 = self.gethei()
        #the second vector.
        absc2 = vector3.getabsc()
        ord2 = vector3.getord()
        hei2 = vector3.gethei()
        if (absc1 == absc2 ) and (ord1 == ord2) and (hei1 == hei2 ):
            return True
        else:
            return False  

    def norm(self): #the vector norm.
        print("the norm of this vector :", ((self._absc**2)+(self._ord**2)+(self._hei**2))**0.5) 
