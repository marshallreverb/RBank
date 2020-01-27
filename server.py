import affiche
import getpass
from db import db


def main(db):
    #initialise db 
    affiche.aff_("************************* ROYALE BANK************************")
    login(db) 

def login(db):
    
    while True :
        us = input("** enter your user name :")
        passw = getpass.getpass("** enter your password :")

        db.c.execute("SELECT * FROM user WHERE username = ? AND email = ?",[us,passw])
        resl = db.c.fetchall()
    
        if  resl:
            for i  in resl:
               affiche.aff_("\t\t\tWelcome {}\t\t\t".format(i[1]))
            break
        else :
           affiche.aff_err("Wrong ! username or password ")

if __name__ == "__main__":
    my_db = db()
    main(my_db)