import psycopg2
class VoteDatabase():
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
