
import itertools
from agent import *

class Situation3:

	def __init__(self,n_items=6): #constructor
		if n_items%3!=0:
			print("Warning: A problem has to be of proportional size regarding the number of agents")
			return
		self._agents=[[],[],[]]
		self.createAgents()
		self._items = [i for i in range(1,n_items+1,1)]
		self._allocations=self.generateAllAlloc()
		self._preferences=list(itertools.permutations(self._items))
		print(self._preferences)

	def createAgents(pref=0):
		if pref==0:
			u_l=items[:]
			u_l=[i[:]]
			for i in range(3):
				self.agent.append(Agent(u_l,[]))
				random.shuffle(u_l)

	def generateAllAlloc(self):
		l1=list(itertools.combinations(self._items,n_items/len(self._agents)))
		l2=[]
		for i in l1:
			for j in l1:
				flag = 0
				for k in j:
					if k in i:
						flag = 1
						break
				if flag == 0:
					l2.append([i,j])
					l2.append([j,i])
		return l2

	def printAlloc(self,n):
		if n<len(self._allocations):
			for j in range(0,len(self._agents)-1):
				print(("agent "+str(j+1)+":"+str(self._allocations[n][j])))
			print("agent "+str(len(self._agents))+":"+str(self.lastAlloc(n)))

	def lastAlloc(self,n):
		"""
		Regarding the allocation of the other agent of the problem, return the allocation of the third agent
		"""
		l=[]
		for i in self._allocations[n]:
			for j in i:
				for k in i:
					l.append(k)
		return tuple([i for i in self._items if i not in l])

	def infos(self):
		print("Number of agents="+str(len(prob._agents)))
		print("Number of items="+str(len(prob._items)))
		print("Items="+str(prob._items))
		print("Possible Allocations="+str(prob._allocations))

if __name__ == '__main__':
	n_items=6
	prob=Situation3(n_items)
	prob.infos()
	prob.printAlloc(2)