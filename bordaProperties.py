from agent import *

def bordaScore(agent):
	N = len(agent.p) #total number of items
	score = 0
	for item in agent.hold:
		score += N + 1 - agent.p[item-1]
	return score

def bordaParetoOptimal(l_agents,alloc):
	score = 0
	for a in l_agents:
		score += bordaScore(a)

def bordaEnvy(l_agents):
	"""
	Return True if envy-free
	"""
	N = len(l_agents[0].p) #total number of items
	#print("N="+str(N))
	for i in range(len(l_agents)):
		l_scores=[]
		for j in range(len(l_agents)):
			score=0
			for item in l_agents[j].hold:
				score += N + 1 - l_agents[i].p[item-1]
			l_scores.append(score)
		l_scores=[ max(0,k-l_scores[i]) for k in l_scores]
		if sum(l_scores)>0:
			return False
	return True

def bordaEnvyWho(l_agents):
	"""
	Just useful for the notebook, do the same than bordaEnvy but show the first jealous agent
	"""
	flag=0
	N = len(l_agents[0].p) #total number of items
	#print("N="+str(N))
	for i in range(len(l_agents)):
		l_scores=[]
		for j in range(len(l_agents)):
			score=0
			for item in l_agents[j].hold:
				score += N + 1 - l_agents[i].p[item-1]
			l_scores.append(score)
		for k in range(3):
			if max(0,l_scores[k]-l_scores[i])!=0:
				print("Agent "+str(i)+" is jealous of agent "+str(k)+".")
				flag=1
	if flag==0:
		"The allocation is envy-free!"

if __name__ == '__main__':
	agents = []
	agents.append(Agent([1,2,3,4,5,6],[1,2])) 
	agents.append(Agent([3,4,1,5,6,2],[3,4]))
	agents.append(Agent([3,2,5,1,4,6],[5,6]))

	i=0
	for a in agents:
	    print("Score agent "+str(i)+": "+str(bordaScore(a)))
	    i+=1

	bordaEnvy
