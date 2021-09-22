class piece:
    def __init__(self,absisse,ordonnee,couleur,classe):
        self.x = absisse
        self.y = ordonnee
        self.couleur = couleur
        self.classe = classe
	

class pion(piece):
    def __str__(self):
        return f"Pion, ({self.x},{self.y})"
    def avancer(self):
        if self.couleur == "blanc":
            deplacement = 1
        else:
            deplacement = -1
        if plateau.contenu_case(self.x,self.y+deplacement)[0] == "empty":
            plateau.plateau_jeu[self.y+deplacement-1][self.x-1] = (self, self.x, self.y+deplacement)
            plateau.plateau_jeu[self.y-1][self.x-1] = ("empty",self.x,self.y)
            self.y += deplacement
        else:
            print("Je ne peux pas avancer")


class Plateau:
    def __init__(self, liste, size):
        self.plateau_jeu = list()
        self.coordonees = {}
        for pion in liste:
            self.coordonees[(pion.x,pion.y)] = pion
        for x in range(1, size+1):
            self.plateau_jeu.append( list() )
            for y in range(1, size+1):
                try:
                    self.plateau_jeu[x-1].append( (self.coordonees[(x,y)],x,y) )
                except:
                    self.plateau_jeu[x-1].append( ("empty",x,y) )
    def __str__(self):
        string = ""
        for y in self.plateau_jeu:
            string += "\n" 
            for x in y:
                string += "|"
                try:
                    string += x[0].classe + " "
                except:
                    string += x[0]
        return string
    def contenu_case(self,x,y):
        try:
            return self.plateau_jeu[x-1][y-1]
        except:
            return "out"

p1 = pion(1,1,'blanc','pion')
p2 = pion(4,4,'noir','pion')
plateau = Plateau([p1,p2],4)
