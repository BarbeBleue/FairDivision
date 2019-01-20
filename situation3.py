
import itertools

class Situation3:

	def __init__(self,n_items=6): #constructor
		if n_items%3!=0:
			print("Warning: A problem has to be of proportional size regarding the number of agents")
			return
		self._n_agents=3
		self._items = [i for i in range(1,n_items+1,1)]
		self._allocations=self.generateAlloc()
		self._preferences=list(itertools.permutations(self._items))
		self._problem=0 

	def generateAlloc(self):
		l1=list(itertools.combinations(self._items,n_items/self._n_agents))
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
			for j in range(0,self._n_agents-1):
				print(("agent "+str(j+1)+":"+str(self._allocations[n][j])))
			print("agent "+str(self._n_agents)+":"+str(self.lastAlloc(n)))

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
		print("Number of agents="+str(prob._n_agents))
		print("Number of items="+str(len(prob._items)))
		print("Items="+str(prob._items))
		print("Allocations="+str(prob._allocations))

if __name__ == '__main__':
	n_items=6
	prob=Situation3(n_items)
	prob.infos()
	prob.printAlloc(2)