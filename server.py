import affiche
import getpass
from db import db


def main(db):
    #initialise db 
    login(db) 

def login(db):
    
    while True :
        us = input("** enter your user name :")
        passw = getpass.getpass("** enter your password :")

        db.c.execute("SELECT * FROM users WHERE username = ? AND emails = ?",us,passw)
        resl = db.c.fetchall()
        
        if  resl:
            for i  in resl:
                affiche.aff_("*Welcome {}".format(i[2]))
            break

if __name__ == "__main__":
    my_db = db()
    main(my_db)