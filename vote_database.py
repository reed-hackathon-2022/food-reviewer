import psycopg2, sqlite3

class PostgreSQLVoteDatabase():
    def __init__(self, database):
        self.con = psycopg2.connect(database)
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS totals (
                item TEXT PRIMARY KEY,
                total INTEGER NOT NULL DEFAULT 0
            );
            ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS votelogs (
                userid TEXT,
                item TEXT,
                vote INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (userid, item)
            );
            ''')
        
    def set(self, user, item, vote):
        self.cur.execute('''
            SELECT total FROM totals WHERE item = %s;
            ''', (item,))
        oldtotaltuple = self.cur.fetchone()
        if oldtotaltuple == None:
            self.cur.execute('''
            INSERT INTO totals (item) VALUES (%s);
            ''', (item,))
            oldtotal = 0
        else:
            oldtotal = oldtotaltuple[0]
            
        self.cur.execute('''
            SELECT vote FROM votelogs WHERE userid = %s AND item = %s;
            ''', (user, item))
        oldvotetuple = self.cur.fetchone() 
        if oldvotetuple == None:
            self.cur.execute('''
            INSERT INTO votelogs (userid, item) VALUES (%s, %s);
            ''', (user, item))
            oldvote = 0
        else:
            oldvote = oldvotetuple[0]
        self.cur.execute('''
            UPDATE totals SET total = %s WHERE item = %s;
            ''', (oldtotal + vote - oldvote, item))
        self.cur.execute('''
            UPDATE votelogs SET vote = %s WHERE userid = %s AND item = %s;
            ''', (vote, user, item))
        
    def get_item(self, item):
        self.cur.execute('''
            SELECT total FROM totals WHERE item = %s;
            ''', (item,))
        totaltuple = self.cur.fetchone()
        if totaltuple == None:
            return 0
        else:
            return totaltuple[0]
    
    def get_single_vote(self, user, item):
        self.cur.execute('''
            SELECT vote FROM votelogs WHERE userid = %s AND item = %s;
            ''', (user, item))
        votetuple = self.cur.fetchone()
        if votetuple == None:
            return 0
        else:
            return votetuple[0]
        
class SQLiteVoteDatabase():
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS totals (
                item TEXT PRIMARY KEY,
                total INTEGER NOT NULL DEFAULT 0
            );
            ''')
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS votelogs (
                user TEXT,
                item TEXT,
                vote INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (user, item)
            );
            ''')
        
    def set(self, user, item, vote):
        oldtotaltuple = self.cur.execute('''
            SELECT total FROM totals WHERE item = ?;
            ''', (item,)).fetchone()
        if oldtotaltuple == None:
            self.cur.execute('''
            INSERT INTO totals (item) VALUES (?);
            ''', (item,))
            oldtotal = 0
        else:
            oldtotal = oldtotaltuple[0]
            
        oldvotetuple = self.cur.execute('''
            SELECT vote FROM votelogs WHERE user = ? AND item = ?;
            ''', (user, item)).fetchone() 
        if oldvotetuple == None:
            self.cur.execute('''
            INSERT INTO votelogs (user, item) VALUES (?, ?);
            ''', (user, item))
            oldvote = 0
        else:
            oldvote = oldvotetuple[0]
        self.cur.execute('''
            REPLACE INTO totals (item, total) VALUES (?, ?);
            ''', (item, oldtotal + vote - oldvote))
        self.cur.execute('''
            REPLACE INTO votelogs (user, item, vote) VALUES (?, ?, ?);
            ''', (user, item, vote))
        
    def get_item(self, item):
        totaltuple = self.cur.execute('''
            SELECT total FROM totals WHERE item = ?;
            ''', (item,)).fetchone()
        if totaltuple == None:
            return 0
        else:
            return totaltuple[0]
    
    def get_single_vote(self, user, item):
        votetuple = self.cur.execute('''
            SELECT vote FROM votelogs WHERE user = ? AND item = ?;
            ''', (user, item)).fetchone()
        if votetuple == None:
            return 0
        else:
            return votetuple[0]
