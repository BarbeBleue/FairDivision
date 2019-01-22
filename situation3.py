
import itertools
import csv
from agent import *
from bordaProperties import *
from problem3 import *



import numpy as np

def bitlist2int(bitlist):
	out = 0
	for bit in bitlist:
		out = (out << 1) | bit
	return out

def betterDictPrint(mydict):
	for key in mydict:
		print("{"+str(key)+" : "+str(mydict[key])+"}")


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

		self.initDatabase()

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
		self.data_allBorda = np.zeros((self._nb_prop+1))

		#Number of generated allocations with Borda properties
		self.data_genBorda = np.zeros((2**self._nb_algo,2**self._nb_prop))


	def fillDatabase(self, info_allocs):
		"""
		@info_allocs : contains useful information for each allocation for a particular set of preferences.
		"""

		nb_allocs = len(info_allocs)
		self.data_allBorda[0:3] = np.array([self._problem._n_BS,self._problem._n_BE,self._problem._n_BM])
		self.data_allBorda[3] += nb_allocs

		for alloc in info_allocs:
			info = info_allocs[alloc]
			indAlgo = bitlist2int(info[5:7])
			indProp = bitlist2int(info[2:5])
			self.data_genBorda[indAlgo][indProp] += 1

	def saveDatabase(self):
		file = open("test.csv","w")
		writer = csv.writer(file,delimiter=",")

		writer.writerow(self.data_allBorda)
		file.write("\n")
		for row in self.data_genBorda:
			writer.writerow(row)


		file.close()




	def run(self):

		prefA = (1,2,3,4,5,6)
		l_empty = [ [] for i in range(0,3)]


		i = 0
		j = 0
		for prefB in self._preferences:
			j=0
			for prefC in self._preferences:

				print("PREFERENCES ({0},{1}):{2}".format(i,j,[prefA,prefB,prefC]))
				

				self._problem.setPreferences([prefA,prefB,prefC])
				self._problem.generateBordaProperties()
				#print(len(self._problem._allocations))
				
				self._problem.setAllocations(l_empty)
				self._problem.solve_all()

				#betterDictPrint(self._problem._allocations)
				self.fillDatabase(self._problem._allocations)
				self.saveDatabase()

				self._problem.reset()

				j += 1

			i += 1				




if __name__ == '__main__':
	n_items=6
	sit=Situation3(n_items)
	#print(sit._problem)
	sit.run()
	