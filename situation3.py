
import itertools
from agent import *
from bordaProperties import *

class Situation3:

	def __init__(self,n_items=6): #constructor
		if n_items%3!=0:
			print("Warning: A problem has to be of proportional size regarding the number of agents")
			return
		self._items = [i for i in range(1,n_items+1,1)]
		self._allocations=self.generateAllAlloc()
		self._preferences=list(itertools.permutations(self._items))
		self._current_pref=[]
		self._agents=[]
		self.createAgents()
		self._maxBordaSum=0
		self._maxminBorda=0

	def createAgents(self):
		for i in range(3):
			self._agents.append(Agent())

	def generateAllAlloc(self):
		l1=list(itertools.combinations(self._items,2))
		l2={}
		for i in l1:
			for j in l1:
				flag = 0
				for k in j:
					if k in i:
						flag = 1
						break
				if flag == 0:
					l=tuple([k for k in range(1,7) if k not in i+j])
					l2[i,j,l]=[]
					l2[j,i,l]=[]
		return l2

	def generateBordaScores(self,l_pref):
		self.setPreferences(l_pref)
		for alloc in self._allocations.keys():
			self.setAllocations(alloc)
			score = 0a
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
			self._allocations[alloc].append(score)
			self._allocations[alloc].append(min_score)

	def propBS(self):
		"""
		maximal Borda sum property
		"""
		for alloc in self._allocations.keys():
			if self._allocations[alloc][0]==self._maxBordaSum:
				self._allocations[alloc].append('BS')

	def propBE(self):
		for alloc in self._allocations.keys():
			self.setAllocations(alloc)
			if bordaEnvy(self._agents):
				self._allocations[alloc].append('BE')
			return


	def propBM(self):
		"""
		max-min Borda property
		"""
		for alloc in self._allocations.keys():
			if self._allocations[alloc][1]==self._maxminBorda:
				self._allocations[alloc].append('BM')

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
		if len(l_pref)!=3:
			print("Warning! l_pref has to be of size 3!")
			return
		for i in range(3):
			self._agents[i].u=l_pref[i]

	def saveProp(self):
		return

	def infos(self):
		print("Number of agents="+str(len(prob._agents)))
		print("Number of items="+str(len(prob._items)))
		print("Items="+str(prob._items))
		print("Possible Allocations="+str(prob._allocations))

if __name__ == '__main__':
	n_items=6
	prob=Situation3(n_items)
	p=[prob._preferences[0],prob._preferences[1],prob._preferences[2]]
	
	d={}
	for i in range(5):
		d[prob._allocations.keys()[i]]=[]
	prob._allocations=d
	prob.generateBordaScores(p)
	prob.propBS()
	prob.propBE()
	prob.propBM()
	print(prob._allocations)
	