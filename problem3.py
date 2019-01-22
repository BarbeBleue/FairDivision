from bordaProperties import *
import itertools
import algorithm

# INDEX OF ALLOCATION LIST
## properties
BS = 2
BE = 3
BM = 4
## algorithms
OS = 5
BU = 6

class Problem3:

	''' 
	a problem with 3 agents is defined by: 
        - a _current_pref of the current preferences of the 3 agents analyzed
        - a dictionary _allocations of all the possible allocations with corresponding properties and algorithms which find them, 
        - a list _agents of 3 Agents
        - a value _maxBordaSum equal to the maximum Borda sum you can get regarding the current set of preferences
        - a value _maxminBorda equal to the maximal minimum Borda score you can get regarding the current set of preferences
        - an initial allocation of resources
        - a visibility topology (symmetric)
        - an exchange topology (directed)
    '''
	def __init__(self,n_items,pref=[]):
		if len(pref)>0 and len(pref)!=3:
			print("Warning! pref has to be of size 3!")
		self._current_p=pref
		self._items=[i for i in range(1,n_items+1,1)]
		self._allocations={}
		self.generateAllAlloc()
		self._agents=[]
		self.createAgents()
		self._maxBordaSum=0
		self._maxminBorda=0
		self._n_BS=0
		self._n_BE=0
		self._n_BM=0

		if len(pref)==3:		
			self.generateBordaProperties()

	def __str__(self):
		string="Current set of preferences: "+str(self._current_p)
		string+="\nItems to share: "+str(self._items)
		string+="\nMaximum Borda Score sum: "+str(self._maxBordaSum)
		string+="\nMaximum Minimum Borda Score: "+str(self._maxminBorda)
		string+="\nNumber of BS : "+str(self._n_BS)
		string+="\nNumber of BE : "+str(self._n_BE)
		string+="\nNumber of BM : "+str(self._n_BM)
		
		return string

	def createAgents(self):
		for i in range(3):
			self._agents.append(Agent())

	def generateAllAlloc(self):
		l1=list(itertools.combinations(self._items,2))
		for i in l1:
			for j in l1:
				flag = 0
				for k in j:
					if k in i:
						flag = 1
						break
				if flag == 0:
					l=tuple([k for k in range(1,7) if k not in i+j])
					self._allocations[i,j,l]=[0]*7
					self._allocations[j,i,l]=[0]*7

	def generateBordaProperties(self):
		self.generateBordaScores()
		self.propBS()
		self.propBE()
		self.propBM()

	def generateBordaScores(self):
		self.setPreferences(self._current_p)
		for alloc in self._allocations.keys():
			self.setAllocations(alloc)
			score = 0
			min_score = 99999
			for a in self._agents:
				score_a=bordaScore(a)
				if score_a<min_score:
					min_score=score_a
				score += score_a
			if score>self._maxBordaSum:
				self._maxBordaSum=score
			if min_score>self._maxminBorda:
				self._maxminBorda=min_score
			self._allocations[alloc][0]=score
			self._allocations[alloc][1]=min_score

	def propBS(self):
		"""
		maximal Borda sum property
		"""
		for alloc in self._allocations.keys():
			if self._allocations[alloc][0]==self._maxBordaSum:
				self._allocations[alloc][BS]=1
				self._n_BS+=1

	def propBE(self):
		for alloc in self._allocations.keys():
			self.setAllocations(alloc)
			if bordaEnvy(self._agents):
				self._allocations[alloc][BE]=1
				self._n_BE+=1


	def propBM(self):
		"""
		max-min Borda property
		"""
		for alloc in self._allocations.keys():
			if self._allocations[alloc][1]==self._maxminBorda:
				self._allocations[alloc][BM]=1
				self._n_BM+=1

	def setAllocations(self,l_alloc):
		"""
		Clear allocations and set new ones to agents
		"""
		if len(l_alloc)!=3:
			print("Warning! l_alloc has to be of size 3!")
			return
		for i in range(3):
			self._agents[i].clearItems()
			self._agents[i].getItems(l_alloc[i])

	def setPreferences(self,l_pref):
		"""
		Set new preferences to agents
		"""
		self._current_p=l_pref
		if len(l_pref)!=3:
			print("Warning! l_pref has to be of size 3!")
			return
		for i in range(3):
			self._agents[i].p=l_pref[i]

	def solve(self, algo):
		if algo == OS:
			allocs = set(OS_3(self._agents))

		elif algo == BU :
			allocs = set(bottomUp_3(self._agents))

		else :
			print("Invalid algo : "+str(algo))

		for alloc in allocs :
			self._allocations[alloc][algo] = 1

	

if __name__ == '__main__':
	prob=Problem3(6)
	p=[(1,2,3,4,5,6),(6,4,2,1,3,5),(3,2,4,1,5,6)]
	d={}
	for i in range(5):
		d[prob._allocations.keys()[i]]=[0]*7
	#prob._allocations=d
	prob.setPreferences(p)
	prob.generateBordaProperties()
	print(prob._allocations)

	print(prob)
	