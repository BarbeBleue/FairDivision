
class Agent(object): 
    

    def __init__(self,preference=[],resources=[]):
        '''
        '''
        self.p = preference # list of agent preferences, from high to low preferences
        self.hold = resources # list of resources held by agent

    def __str__(self):
        string="Preferences: "+str(self.p)
        string+="\nRessources: "+str(self.hold)
        return string
        
    def getItem(self,r):
        '''
        @r: a single item
        '''
        self.hold.append(r)
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
        return
        
    def dropItems(self,lr):
        for r in lr:
            self.dropItem(r)
        return
        
    def clearItems(self):
        self.hold=[]

    def h(self,l,U):
        """
        @l : minimum rank, from 1 to N
        @U : list of unallocated items
        """
        H=[]
        for resource in U :
            if resource in self.p[0:l] :
                H.append(resource)
        #print("h : U="+str(U)+", l="+str(l)+",H="+str(H))
        return H        

    def lastU(self,U):
        """
        @U : list of unallocated items
        """
        for item in reversed(self.p) :
            if item in U : 
                return item


        
    #TODO: replace by dropItems      

if __name__ == '__main__':
    a = Agent([1,2,3,4,5,6],[])

    print(a.lastU([1,2,3,6]))

    #a.h(3,[1,2,3,4,5,6])

    