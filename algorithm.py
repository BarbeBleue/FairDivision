# coding: utf-8
import copy

from agent import Agent


def OS_3(agents):
	"""
	Sequential algorithm for 3 agents.
	Returns all possible allocations.
	"""

	print("OS for 3 agents")
	return OS_3_rec(agents, U=[1,2,3,4,5,6], l=1)

	
def OS_3_rec(agents, U, l):
	"""
	@agent: agent class with preferences and allocated items
	@U : unallocated items
	@l : invocation level
	"""
	#print("in os_3_rec : "+str(l))

	if not U : #Allocation found
		for a in agents :
			a.hold.sort()
		res = [(tuple(agents[0].hold), tuple(agents[1].hold),tuple(agents[2].hold))]
		#print("found:"+str(res))
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
	"""
	Bottom up algorithm for 3 agents
	"""
	print("BottomUp for 3 agents")

	alloc = []
	alloc += bottomUp_3_rec(copy.deepcopy(agents),[1,2,3,4,5,6],0)
	alloc += bottomUp_3_rec(copy.deepcopy(agents),[1,2,3,4,5,6],1)
	return alloc


def bottomUp_3_rec(agents,U,direction):
	"""
	@agent: agent class with preferences and allocated items
	@U : unallocated items
	@direction : 0 = give last item to left agent
				 1 = give last item to right agent
	"""
	#print("U="+str(U))

	if not U : #Allocation found
		for a in agents :
			a.hold.sort()
		res = [(tuple(agents[0].hold), tuple(agents[1].hold),tuple(agents[2].hold))]
		#print("found:"+str(res))
		return res

	alloc = []

	#Allocate this turn
	for i in range(0,len(agents)) :
		if direction == 0 :
			next_i = (i-1)%3
		else :
			next_i = (i+1)%3

		item = agents[i].lastU(U)
		agents[next_i].getItem(item)
		U.remove(item)

	alloc += bottomUp_3_rec(copy.deepcopy(agents),copy.copy(U),0)
	alloc += bottomUp_3_rec(copy.deepcopy(agents),copy.copy(U),1)

	return alloc

def trump_3(agents):
	"""
	Trump algorithm for 3 agents

	Pb : comment adapter pour 3 agents ?? 
		lorsque A donne le pire des meilleurs B à B, C peut être jaloux.
	"""
	print("Trump for 3 agents")





if __name__ == '__main__':

	agents = []
	agents.append(Agent([1,2,3,4,5,6],[]))
	agents.append(Agent([3,4,1,5,6,2],[]))
	agents.append(Agent([3,2,5,1,4,6],[]))
	
	#res = OS_3(agents)
	res = bottomUp_3(agents)

	print("Possible allocations: ")
	print(res)
	