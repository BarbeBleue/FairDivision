
class Agent(object): 
    
    def __init__(self,utility=[],resources=[]):
        '''
        '''
        self.u= utility # dictionary of utility for resources
        self.hold = resources # list of resources held by agent
        self.current_u = sum([self.u[r] for r in resources]) # current utility enjoyed by agent
        
    def __str__(self):
        string="Utilities: "+str(self.u)
        string+="\nRessources: "+str(self.hold)
        return string
        
    def getItem(self,r):
        '''
        @r: a single item
        '''
        self.hold.append(r)
        self.current_u += self.u[r-1]
        return
        
    def getItems(self,lr):
        '''
        @lr: a list of items
        '''
        for r in lr:
            self.getItem(r)
        return
        
    def dropItem(self,r):
        if r not in self.hold:
            print ("agent ", self, " does not hold ", r, "!!!")
        self.hold.remove(r)
        self.current_u -= self.u[r]
        return
        
    def dropItems(self,lr):
        for r in lr:
            self.dropItem(r)
        return
        
    def clearItems(self):
        self.hold=[]
        self.current_u = 0

    def h(self,l,U):
        H=[]
        for item in U:
            if self.u[item-1]<=l:
                H.append(item)
        return H

        
    #TODO: replace by dropItems        
    