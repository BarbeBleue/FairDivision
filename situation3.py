
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
		file = open("save.csv","w")
		writer = csv.writer(file,delimiter=",")

		writer.writerow(self.data_allBorda)
		file.write("\n")
		for row in self.data_genBorda:
			writer.writerow(row)


		file.close()

	def printResults(self):

		buf = ""
		sp = 10
		prop_names = ["BS","BE","BM"]
		algo_names = ["OS","BU"]

		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print("Fraction of allocations with Borda properties")
	
		l = len(self.data_allBorda)
		for s in prop_names :
			buf += s.ljust(sp)
		buf += "Total".ljust(sp)
		buf += "\n"
		for d in self.data_allBorda:
			buf += str(int(d)).ljust(sp)
		buf += "\n"
		for d in self.data_allBorda:
			buf += (str(round(100*d/self.data_allBorda[l-1], 2)) + "%").ljust(sp)
		buf += "\n"
		print(buf)


		buf = ""
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print("Generated allocations with Borda properties")
		buf += "".ljust(sp) 
		buf += "None".ljust(sp)+"BM".ljust(sp)+"BE".ljust(sp)+"BM+BE".ljust(sp)
		buf += "BS".ljust(sp)+"BS+BM".ljust(sp)+"BS+BE".ljust(sp)+"All".ljust(sp)
		buf += "\n"
		l2 = ["None"]+algo_names+["Both"]
		h,w = self.data_genBorda.shape
		for i in range(0,h):
			buf += str(l2[i]).ljust(sp)
			for j in range(0,w):
				buf += str(int(self.data_genBorda[i][j])).ljust(sp)
			buf += "\n"
		print(buf)

	def printResultsAllProperties(self):
		buf = ""
		sp = 10
		prop_names = ["BS","BE","BM"]
		algo_names = ["OS","BU"]

		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print("Fraction of generated allocation with all Borda properties")
		frac_OS = (self.data_genBorda[1,7]+self.data_genBorda[3,7])/sum(self.data_genBorda[:,7])
		frac_BU = (self.data_genBorda[2,7]+self.data_genBorda[3,7])/sum(self.data_genBorda[:,7])

		buf += "".ljust(sp) + "6 items".ljust(sp) + "\n"
		buf += "OS".ljust(sp) + (str(round(100*frac_OS,2))+"%").ljust(sp) + "\n"
		buf += "BU".ljust(sp) + (str(round(100*frac_BU,2))+"%").ljust(sp) + "\n"
		print(buf)


	def loadResults(self,filename):
		f = open(filename,"r")
		reader = csv.reader(f,delimiter=',')

		self.data_genBorda = []
		ind = 0
		for row in reader:
			if row :
				if ind == 0:
					self.data_allBorda = np.array([float(e) for e in row])
					ind += 1
				else :
					self.data_genBorda.append(np.array([float(e) for e in row]))

		self.data_genBorda = np.array(self.data_genBorda)

	def run(self,nb_iter=-1,verbose=True):

		prefA = (1,2,3,4,5,6)
		l_empty = [ [] for i in range(0,3)]


		i = 0
		j = 0
		for prefB in self._preferences:
			j=0
			for prefC in self._preferences:

				if verbose:
					print("PREFERENCES ({0},{1}):{2}".format(i,j,[prefA,prefB,prefC]))
				

				self._problem.setPreferences([prefA,prefB,prefC])
				self._problem.generateBordaProperties()
				#print(len(self._problem._allocations))
				
				self._problem.setAllocations(l_empty)
				self._problem.solve_all(verbose=False)

				#betterDictPrint(self._problem._allocations)
				self.fillDatabase(self._problem._allocations)
				

				self._problem.reset()

				j += 1

				if (i*len(self._preferences)+j) > nb_iter and (nb_iter != -1):
					return

			i += 1	
			self.saveDatabase()			




if __name__ == '__main__':
	n_items=6
	sit=Situation3(n_items)
	#print(sit._problem)
	sit.run(nb_iter=100,verbose=False)
	sit.printResults()
	sit.loadResults("csv/complete_first_try.csv")
	sit.printResults()
	sit.printResultsAllProperties()
	