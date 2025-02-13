class Parc:
    def __init__(self,id,adresse,capacite):
        self.id = id 
        self.adresse = adresse
        self.capacite = capacite
        self.Voitures = []

    def entrerVoiture(self,Voiture):
        """entrez la voiture """
        if len(self.Voitures) < self.capacite :
            self.Voitures.append(Voiture)
            print(f"la voiture {Voiture.matricule} est dans le parc") 

        else:
            print(f"il n'y a plus d'espace disponible")

    
    def calculerNbrPlacesLibres(self):
        """calculer nombre voiture"""
        Place_disponible = self.capacite - len(self.Voitures) 
        print(f"il reste {Place_disponible} place(s) disponible")
    
    

    def sortirVoiture(self,Voiture):
        self.Voitures.remove(Voiture)
        print(f"la voiture {Voiture.matricule} est sortie du parc")

        self.calculerNbrPlacesLibres()
        return 

        

            




class Voiture : 
    def __init__(self,matricule,marque,couleur):
        self.matricule = matricule
        self.marque = marque 
        self.couleur = couleur

    def afficherInfo(self):
        """afficher les informations"""

        print(self.matricule)
        print(self.marque)
        print(self.couleur) 

        
P1 = Parc(1,"wood street",3)

V1 = Voiture(1067,"Rav4","Rouge") 
V2 = Voiture(1057,"RangeRover","noir")
V3 = Voiture(1047,"Prado","gris")
V4 = Voiture(1037,"limozine","blanc") 

P1.entrerVoiture(V1) 
P1.entrerVoiture(V2)
P1.entrerVoiture(V3)
P1.entrerVoiture(V4)

P1.sortirVoiture(V1) 



