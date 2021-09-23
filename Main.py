class piece:
    def __init__(self,absisse,ordonnee,couleur):
        self.x = absisse
        self.y = ordonnee
        self.couleur = couleur
	

class pion(piece):
    def __init__(self,absisse,ordonnee,couleur):
        self.classe = 'pion'
        super().__init__(absisse,ordonnee,couleur)

    def __str__(self):
        return f"Pion, ({self.x},{self.y})"

    def avancer(self):
        if self.couleur == "blanc":
            self.mouvement(0,1)
        else:
            self.mouvement(0,-1)

    def droite(self):
        self.mouvement(1,0)

    def gauche(self):
        self.mouvement(-1,0)

    def mouvement(self,deplacement_x, deplacement_y):
        if plateau.contenu_case(self.x+deplacement_x,self.y+deplacement_y)[0] == "empty":
            plateau.plateau_jeu[self.y+deplacement_y-1][self.x+deplacement_x-1] = (self, self.x+deplacement_x, self.y+deplacement_y)
            plateau.plateau_jeu[self.y-1][self.x-1] = ("empty",self.x,self.y)
            self.y += deplacement_y
            self.x += deplacement_x
            print(self)
            print(plateau)
        elif type(plateau.contenu_case(self.x+deplacement_x,self.y+deplacement_y)[0]) == pion and plateau.contenu_case(self.x+deplacement_x,self.y+deplacement_y)[0].couleur != self.couleur:
            print('je peux manger')
        else:
            print("Je ne peux pas avancer")


class Plateau:
    def __init__(self, liste, size):
        self.plateau_jeu = list()
        self.coordonees = {}
        for pion in liste:
            self.coordonees[(pion.x,pion.y)] = pion
        for y in range(1, size+1):
            self.plateau_jeu.append( list() )
            for x in range(1, size+1):
                try:
                    self.plateau_jeu[y-1].append( (self.coordonees[(x,y)],x,y) )
                except:
                    self.plateau_jeu[y-1].append( ("empty",x,y) )

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
            assert x!=0 and y!=0
            return self.plateau_jeu[y-1][x-1]
        except:
            return "out"

p1 = pion(1,1,'blanc')
p2 = pion(1,2,'noir')
p3 = pion(4,4,'noir')
p4 = pion(4,3,'noir')
plateau = Plateau([p1,p2,p3,p4],4)
print(plateau)
