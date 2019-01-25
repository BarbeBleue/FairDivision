
import itertools
from agent import *
from bordaProperties import *
from problem3 import *



import numpy as np

def bitlist2int(bitlist):
	out = 0
	for bit in bitlist:
		out = (out << 1) | bit
	return out

class Situation3:

	''' 
	a situation with 3 agents is defined by: 
        - a list _items of n_items to share,
        - a list _preferences of all the possible arrangement of preferences for a single agent
        - a problem _problem
    '''

	def __init__(self,n_items=6): #constructor
		if n_items%3!=0:
			print("Warning: A problem has to be of proportional size regarding the number of agents")
			return
		self._n_items = n_items
		self._preferences=list(itertools.permutations([i for i in range(1,n_items+1,1)]))
		self._problem=Problem3(n_items,[])

	def infos(self):
		print("Number of agents="+str(len(prob._agents)))
		print("Number of items="+str(len(prob._items)))
		print("Items="+str(prob._items))
		print("Possible Allocations="+str(prob._allocations))

	def initDatabase(self):
		self._nb_prop = 3
		self._nb_algo = 2

		#Number of allocations with Borda properties
		#self.l_alloc_bordaProp = np.zeros((1,self._nb_prop+1))

		#Number of generated allocations with Borda properties
		self.l_genAlloc_bordaProp = np.zeros((self._nb_algo,2**self._nb_prop))


	def saveDatabase(self, prop_allocs, algo_allocs):
		"""
		@pref_allocs : dict of preference for each alloc
		@algo_allocs : list allocs for each algo
		"""

		"""
		for key,value in pref_allocs.iteritems():
			l1 = value[2:2+self._nb_prop]
			for i in range(0,len(l1)):
				self.l_alloc_bordaProp[i] += l[i]

			if sum(l1) == len(l1):
				self.l_alloc_bordaProp[self._nb_prop] += 1
		"""

		for indAlgo in range(0,len(algo_allocs)):
			allocs = set(algo_allocs[i])
			for a in allocs :
				#Find properties of this alloc
				indProp = bitlist2int(pref_allocs[a][2:2+self._nb_prop])
				
				#Fill algo x prop matrix
				self.l_genAlloc_bordaProp[indAlgo][indProp] += 1

		


if __name__ == '__main__':
	n_items=9
	BE=0
	BS=0
	BM=0
	#for n_items in range(6,13,3):
	sit=Situation3(n_items)
	#print(len(sit._problem._allocations))
	l=len(sit._preferences)
	print(l)
	#print(l*l)
	i=0
	p1=sit._preferences[0]
	for p2 in sit._preferences:
		for p3 in sit._preferences:
			i+=1
			sit._problem.setPreferences([p1,p2,p3])
			sit._problem.generateBordaProperties()
			BS+=sit._problem._n_BS
			BE+=sit._problem._n_BE
			BM+=sit._problem._n_BM

			#print("i="+str(i))
		#print(sit._problem)
		
		print("i="+str(i))
		print("BS="+str(BS))
		print("BE="+str(BE))
		print("BM="+str(BM))
	
	BS=BS/(i*90.0)*100
	BE=BE/(i*90.0)*100
	BM=BM/(i*90.0)*100
	print("BS="+str(BS))
	print("BE="+str(BE))
	print("BM="+str(BM))
	

		