class piece:
  def __init__(self,absisse,ordonnee,couleur):
    self.x = absisse
    self.y = ordonnee
    self.couleur = couleur
	
		

class pion(piece):
    def __str__(self):
        return f"Pion, ({self.x},{self.y})"
    def deplacement(self):
        if self.couleur == "blanc":
            deplacement = -1
        else:
            deplacement = 1
        if plateau.contenu_case(self.x,self.y+deplacement) == "empty":
            print("avance")
        else:
            print("Je ne peux pas avancer")
    

class Plateau:
    def __init__(self, liste, size):
        self.pion = list()
        self.coordonees = dict()
        for y in range(1, size+1):
            self.pion.append( list() )
            for x in range(1, size+1):
                try:
                    self.pion[y-1].append( (self.coordonees[(x,y)],x,y) )
                except:
                    self.pion[y-1].append( ("empty",x,y) )
    def __str__(self):
        return str(self.pion) + str(self.coordonees)
    def contenu_case(self,x,y):
        try:
            return self.pion[x-1][y-1]
        except:
            return "empty"

p1 = pion(1,1,'blanc')
p2 = pion(4,4,'noir')
plateau = Plateau([p1,p2],4)
