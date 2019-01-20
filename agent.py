
class Agent(object): 
    
    def __init__(self,utility,resources):
        '''
        '''
        self.u= utility # dictionary of utility for resources
        self.hold = resources # list of resources held by agent
        self.current_u = sum([self.u[r] for r in resources]) # current utility enjoyed by agent
        
    def __str__(self):
        return str(self.u)
        
    def getItem(self,r):
        '''
        @r: a single item
        '''
        self.hold.append(r)
        self.current_u += self.u[r]
        return
        
    def getItems(self,lr):
        '''
        @lr: a list of items
        '''
        for r in lr:
            self.getItem(r)
        return
        
    def giveItem(self,r):
        if r not in self.hold:
            print ("agent ", self, " does not hold ", r, "!!!")
        self.hold.remove(r)
        self.current_u -= self.u[r]
        return
        
    def giveItems(self,lr):
        for r in lr:
            self.giveItem(r)
        return
        
    def dropItems(self):
        self.hold=[]
        self.current_u = 0
        
    #TODO: replace by dropItems        
    