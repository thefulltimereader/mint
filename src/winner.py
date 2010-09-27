'''
Created on Sep 25, 2010
Assignment 1: Mint Problem: 
Given: Multiple of 5 cents (any 5c multiple) price is
       N times more likely than a non-multiple of 5cents.
Design a set of 5 coin denominations for US $ s.t.:
    1. The number of coins required for 'Exact Change" is minimized
    2. Another set of 5 coin denominations s.t. Exchange Number is minimized
 
 Score: score = sum of the costs of all !5mult+ sum of N*costs of 5mult
              = 
         
@author: ajk377
'''

#cost = [float('inf')]*100;
import time, math, sys
counter=0

maxN = 100
def calcCost(d, cost):
    cost[0]=0
    for i in xrange(1, maxN):
        if(cost[i] == float('inf')): 
            minList = []
            for index in xrange(len(d)):
                if i-d[index] > 0:
                    minList += [cost[(i-d[index])] ]
            cost[i] = 1+ min(minList)
    #print cost
    return cost
    
def calcCostOld(cost):
    cost[0]=0
    for i in xrange(2, maxN):
        if cost[i]==float('inf'):
            for j in range(1, i):
                #print "looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                if(cost[j]+cost[i-j] < cost[i]):
                    cost[i]=cost[j]+cost[i-j]
                  #  print "at i: ",i," looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                  #  print "cost[",i,"] is now ", cost[i]
    print cost
def getAvgCost(cost):
    total = score=0.0
    for i in range(1, maxN):
        total+= cost[i]
   #     print "# of coins for ", i," is ", cost[i];
        if i % 5 is 0:
            score+=cost[i]*float(n)
        else:
            score+=cost[i]
    #print "total:",total,"avg cost:",(total/(len(cost)-1)) ,"\n score: ", score;
    return (score, (total/(len(cost)-1)));
'''
    Eliminating search space:
     (A: given an upper bound, B, which the highest # of coins needed to pay
        any amount from 1-99cent, you must have a coin at least total/B.
        i.e. if B = 4, your denomination must have 25. 
        i.e. if maxN{denom}<25, useless.
        Say B = 5, you must have a 20)
     B: Who needs [1,2,3,4,9], or [1,2,3,4,99]?. Given d=[d1,d2,d3,d4,d5]
        Esp the distance bewteen d4, d5 should be big enough.
        Idea of Fast foward: when evaluating every x for [d1,d2,d3,d4,x]. If
        [d1,d2,d3,d4,x-1] does not do well, instead of incrementing  by 1, 
        fast forward. It's probably not because of the x, but the set [d1,d2,d3,d4]
        What is "not doing well"? have a running avg score so far, if that set 
        [d1,d2,d3,d4] does not go above the running avg, fast forward
        = i.e. TAKE THE WINNERS OF SMALLER SET
      C: Do we need any coin bigger than .50??  Say there exists d5=.75, it is 
        good for the last quarter of a dollar, we can use the first quarter to calculate the last quarter,
        but if 50cent coin allows us to use half of to copy over to the second half.
        i.e. with 75cent, you can copy the first 1/4, to the last 1/4 with all val +1
        with 50cent, you can copy the first 1/2 to the last 1/2 with all val +1, 
        50cent is much more space efficient 
'''

def initCost(denom):
    cost = [float('inf')] * maxN
    for i in xrange(len(denom)):
        cost[denom[i]]=1
    return cost

def nextBest(lastWinner):
    global counter
    bestScore = (float('inf'), float('inf'))
    bestCost = []
    bestSoFar = []
    for i in xrange(lastWinner[len(lastWinner)-1], maxN/2):
        tryDenom = lastWinner+[i]
        cost = initCost(tryDenom)
        counter += 1
        calcCost(tryDenom, cost)
        #print "for ", tryDenom
        result = getAvgCost(cost)
        if result[0] < bestScore[0]:
            bestScore = result
            bestSoFar = tryDenom
            bestCost = cost
            #print "bestCost!! %s" % bestCost
    #print "With N=%s and %s denom, the best score is: %s with avg # of coins:%s with denomination: %s" %(n, len(lastWinner)+1, bestScore[0], bestScore[1],bestSoFar)
    #print "With best cost %s"%bestCost
    return (bestSoFar, bestScore)

def nextWinners(lastWinners):
    global counter
    newWinners =  [([],(float('inf'), 1)),([],(float('inf'), 1)),([],(float('inf'), 1))]
    bestScore = [(float('inf'), float('inf'))]
    bestCost = []
    bestSoFar = []
    for eachWinner in lastWinners:
        #eachWinner is a tuple of ([denom], (score,avg))
        thisDenom = eachWinner[0]
        for i in xrange(thisDenom[len(thisDenom)-1], maxN/2):
            tryDenom = thisDenom+[i]
            cost = initCost(tryDenom)
            counter += 1
            calcCost(tryDenom, cost)
            #result has [ (score), (avg)]
            result = getAvgCost(cost)
            contestant = (tryDenom, result)
            #print contestant
            newWinners = getTop3(contestant, newWinners, i)
            #print "bestCost!! %s" % bestCost
    #print "With N=%s and %s denom, the best score is: %s with avg # of coins:%s with denomination: %s" %(n, len(lastWinner)+1, bestScore[0], bestScore[1],bestSoFar)
    #print "With best cost %s"%bestCost
    return newWinners#(bestSoFar, bestScore)
'''
    winner is in tulple (bestDenomSoFar, itsScore)
    add it to the list of bestWinners, sort by their score 
    and take the top 3
'''
def getTop3(winner, bestWinners, i):
    #winner = ([1,10], (900.0, 9))
    #bestWinners = [([],(float('inf'), 1)),([],(float('inf'), 1)),([],(float('inf'), 1))]
    bestWinners+=[winner]
    #if i==11 or i==10 or i==9: print "with", i,"before sort: ", bestWinners
    bestWinners= list(sorted(bestWinners, key=lambda item:item[1][0],  reverse=True))
    #if i==11 or i==10 or i==9:print "with",i,"after sort: ", bestWinners[1:]
    return bestWinners[1:]

def test():
    global n
    n= 50
    bestTwos = nextWinners([ ([1], (0,0)) ])
    print "bestTwos:", bestTwos
    bestThrees = nextWinners(bestTwos)
    print "bestThrees:", bestThrees
    bestFours = nextWinners(bestThrees)
    print "bestFours:", bestFours
    bestFives = nextWinners(bestFours)
    print "best5s:", bestFives
    print "the best is:", bestFives[2:]
    
def tryAll(arg1):
    global counter, n
    n = arg1
    counter = 0
    bestTwo= nextBest([1])
    bestThree = nextBest(bestTwo[0])
    bestFour = nextBest(bestThree[0])
    bestFive = nextBest(bestFour[0])
    
    print "With N=%s the best denom is %s with score:%s, avg:%s"%(n, bestFive[0], bestFive[1][0], bestFive[1][1])
    #print "Looked at %s denominations" % counter
    
def main():
 #   n = raw_input("What's the N?")
    global n
    n = sys.argv[1]
    start = time.clock()
    tryAll(n)
    print "It took", (time.clock()-start),"seconds to complete"
    print "now:", time.clock(), "start:", start
 
    
if __name__ == '__main__':
    main();
    