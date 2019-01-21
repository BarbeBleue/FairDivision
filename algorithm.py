#coding : utf-8
import copy

from agent import Agent


def OS_3(agents):
	"""
	Sequential algorithm for 3 agents.
	Returns all possible allocations.
	"""

	return OS_3_rec(agents, U=[1,2,3,4,5,6], l=1)

	
def OS_3_rec(agents, U, l):
	"""
	@agent: agent class with preferences and allocated items
	@U : unallocated items
	@l : invocation level
	"""
	#print("in os_3_rec : "+str(l))

	if not U : #Allocation has been found
		res = [(tuple(agents[0].hold),tuple(agents[1].hold),tuple(agents[2].hold))]
		print("found:"+str(res))
		return res

	alloc = []

	#Find possible allocations
	Ha = agents[0].h(l,U)
	Hb = agents[1].h(l,U)
	Hc = agents[2].h(l,U)
	combi = combinations(Ha,Hb,Hc)
	#print("combi ="+str(combi))

	#Allocations found
	if combi :
		for c in combi:
			acopy = copy.deepcopy(agents)
			Ucopy = copy.copy(U)

			#Allocate
			for i in range(0,3):
				acopy[i].getItem(c[i])
				Ucopy.remove(c[i])

			#Recursion
			alloc += OS_3_rec(acopy, Ucopy, l+1)

	#No allocations, continue with l+1
	else :
		alloc += OS_3_rec(agents,U,l+1)

	return alloc


def combinations(Ha,Hb,Hc):
	"""
	Gives all possible combination of items from 3 lists
	"""

	c = []
	for i in Ha :
		for j in Hb :
			for k in Hc :
				if (i!=j) and (j!=k) and (i!=k):
					#print(str(i)+","+str(j)+","+str(k))
					c.append((i,j,k))

	return c

def bottomUp_3(agents):



if __name__ == '__main__':
	combinations([4],[1,2],[1,3])

	agents = []
	agents.append(Agent([1,2,3,4,5,6],[]))
	agents.append(Agent([3,4,1,5,6,2],[]))
	agents.append(Agent([3,2,1,5,4,6],[]))

	
	res = OS_3(agents)
	print("Possible allocations: ")
	print(res)
	