
import itertools
from agent import *
from bordaProperties import *
from problem3 import *



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

if __name__ == '__main__':
	n_items=6
	sit=Situation3(n_items)
	print(sit._problem)
	