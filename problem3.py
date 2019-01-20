
import itertools

import random

class Problem3:

	def __init__(self,n_items=6,pref=0): #constructor
		if pref==0:
			self._preferences=aleaPref()
		else:
			self._preferences=pref
		self._allocations=[[],[],[]]

	def infos(self):
		for i in range(3):
			print("agent "+str(i+1)+":")
			print("-preferences "+str(self._preferences[i]))
			print("-allocation "+str(self._allocations[i]))

def aleaPref():
	items=[i for i in range(1,n_items+1,1)]
	p=[items[:]]
	for i in range(2):
		random.shuffle(items)
		p.append(items[:])
		print(p)
	return p

if __name__ == '__main__':
	n_items=6
	prob=Problem3(n_items)
	prob.infos()