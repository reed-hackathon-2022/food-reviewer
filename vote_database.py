import psycopg2, sqlite3

class PostgreSQLVoteDatabase():
    def __init__(self, database):
        self.con = psycopg2.connect(database)
        cur = self.con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS totals (
                item TEXT PRIMARY KEY,
                total INTEGER NOT NULL DEFAULT 0
            );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS votelogs (
                userid TEXT,
                item TEXT,
                vote INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (userid, item)
            );
            ''')
        
    def set(self, user, item, vote):
        cur.execute('''
            SELECT total FROM totals WHERE item = %s;
            ''', (item,))
        oldtotaltuple = cur.fetchone()
        if oldtotaltuple == None:
            cur.execute('''
            INSERT INTO totals (item) VALUES (%s);
            ''', (item,))
            oldtotal = 0
        else:
            oldtotal = oldtotaltuple[0]
            
        cur.execute('''
            SELECT vote FROM votelogs WHERE userid = %s AND item = %s;
            ''', (user, item))
        oldvotetuple = cur.fetchone() 
        if oldvotetuple == None:
            cur.execute('''
            INSERT INTO votelogs (userid, item) VALUES (%s, %s);
            ''', (user, item))
            oldvote = 0
        else:
            oldvote = oldvotetuple[0]
        cur.execute('''
            UPDATE totals SET total = %s WHERE item = %s;
            ''', (oldtotal + vote - oldvote, item))
        cur.execute('''
            UPDATE votelogs SET vote = %s WHERE userid = %s AND item = %s;
            ''', (vote, user, item))
        
    def get_item(self, item):
        cur.execute('''
            SELECT total FROM totals WHERE item = %s;
            ''', (item,))
        totaltuple = cur.fetchone()
        if totaltuple == None:
            return 0
        else:
            return totaltuple[0]
    
    def get_single_vote(self, user, item):
        cur.execute('''
            SELECT vote FROM votelogs WHERE userid = %s AND item = %s;
            ''', (user, item))
        votetuple = cur.fetchone()
        if votetuple == None:
            return 0
        else:
            return votetuple[0]
        
class SQLiteVoteDatabase():
    def __init__(self, path):
        self.con = sqlite3.connect(path, check_same_thread=False)
        cur = self.con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS totals (
                item TEXT PRIMARY KEY,
                total INTEGER NOT NULL DEFAULT 0
            );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS votelogs (
                user TEXT,
                item TEXT,
                vote INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (user, item)
            );
            ''')
        self.con.commit()
        
    def set(self, user, item, vote):
        cur = self.con.cursor()
        oldtotaltuple = ur.execute('''
            SELECT total FROM totals WHERE item = ?;
            ''', (item,)).fetchone()
        if oldtotaltuple == None:
            cur.execute('''
            INSERT INTO totals (item) VALUES (?);
            ''', (item,))
            oldtotal = 0
        else:
            oldtotal = oldtotaltuple[0]
            
        oldvotetuple = cur.execute('''
            SELECT vote FROM votelogs WHERE user = ? AND item = ?;
            ''', (user, item)).fetchone() 
        if oldvotetuple == None:
            cur.execute('''
            INSERT INTO votelogs (user, item) VALUES (?, ?);
            ''', (user, item))
            oldvote = 0
        else:
            oldvote = oldvotetuple[0]
        cur.execute('''
            REPLACE INTO totals (item, total) VALUES (?, ?);
            ''', (item, oldtotal + vote - oldvote))
        cur.execute('''
            REPLACE INTO votelogs (user, item, vote) VALUES (?, ?, ?);
            ''', (user, item, vote))
        self.con.commit()
        
    def get_item(self, item):
        cur = self.con.cursor()
        totaltuple = cur.execute('''
            SELECT total FROM totals WHERE item = ?;
            ''', (item,)).fetchone()
        if totaltuple == None:
            return 0
        else:
            return totaltuple[0]
    
    def get_single_vote(self, user, item):
        cur = self.con.cursor()
        votetuple = cur.execute('''
            SELECT vote FROM votelogs WHERE user = ? AND item = ?;
            ''', (user, item)).fetchone()
        if votetuple == None:
            return 0
        else:
            return votetuple[0]
