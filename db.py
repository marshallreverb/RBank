import sqlite3 as sq
import affiche

class db:
    SQL_PATH = "data_db.db"
    conn = None
    c = None

    def __init__(self,):
        self.conn = sq.connect(database = self.SQL_PATH)
        self.c = self.conn.cursor()

    def execute(self,sql_commande,*params):
        try :
            if sql_commande !=  "":
                self.c.execute(sql_commande)
                self.conn.commit()
        except sq.OperationalError:
            affiche.aff_err('Execute: can not connect db') 

    def close(self):
        self.conn.close()