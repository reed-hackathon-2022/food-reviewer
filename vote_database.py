from collections import defaultdict

class VoteDatabase():
    def inner_constructor(): #need to do this or pickle won't work
        return defaultdict(int)
    
    def __init__(self):
        self.totals = defaultdict(int)
        self.votelogs = defaultdict(self.inner_constructor)
        
    def set(self, user, item, value):
        oldvalue = self.votelogs[user][item]
        self.totals[item] += value - oldvalue
        self.votelogs[user][item] = value
        
    def get_item(self, item):
        return self.totals[item]
    
    def get_single_vote(self, user, item):
        return self.votelogs[user][item]

    def audit_totals(self): #checks consistency of vote totals, possibly slow
        return all(self.totals[item] == sum(self.votelogs[user][item] for user in self.votelogs) for item in self.totals)
        
