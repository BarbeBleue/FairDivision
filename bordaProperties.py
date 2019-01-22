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


def maximalBordaSum(agent):
		return

def bordaEnvy(l_agents):
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


