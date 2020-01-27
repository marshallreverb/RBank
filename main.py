#creation de l'interface utilisateur 
#creation de l'interace serveur 
# creation de la base de donnée

import getpass
import affiche

def main():
    k = 0
    
    while True :
        affiche.aff_("Bienvenue a RB","1 . connexion a mon compte ","2 . Ouvrir un nouveau compte")
        a = int(input(":>"))
        if (a == 1 or a == 2):
            break
        affiche.aff_err("Chois non valide ! Veuillez choisir entre 1 ou 2 :")

    #connexion client 
    while True :
        #TODO add restricton to client connexion 
        user  = input("*** entrez votre nom d'utilisateur : ")
        passw = getpass.getpass("***entrez votre mot de passe : ")
        #check for validity
        
if __name__ == "__main__":
    main()
