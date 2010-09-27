'''
Created on Sep 26, 2010
Exchange problem
@author: ajk377
Let the Exchange Number of a purchase be the # of coins given from the 
buyer -> the seller + the # of coins given in change to the buyer -->the seller. 
Assume the availability of 1 dollar. 
 i.e.the Exchange Number for 99 cents is 1 since a penny is returned 
 after handing the seller 1 dollar. 
Your second job is to design a set of 5 coin denominations s.t. 
the Exchange Number of coins required for a purchase is minimized given N

IDEA: The optimal answer may not require a penny depending on N.
Since we're not assuming the existence of a penny, we need to check at certain
points, whether that denomination actually works.
Things to consider:
    1. You can assume the availability of a dollar bill
        => There exists an additive reciprocal of you
            i.e if I am a 70cent, my inverse is 30cent, i want the min of two
        - idea: given a price, find a denomination that is higher than the price
            see the change, and see the minimum
    2. We don't have to have a penny, but we always have 1.00.
        isn't 50Cent like our penny..? that's where everything folds in to sym
'''
import time, math, sys, winner

maxN = 100

'''Want to check, given a cost c,:
    1. get all d in denom that is bigger than c, 
    get the difference or the change
    2. for each change we get, figure out 
    if the exact cost for the change +1 (for the initial) < exact cost of c
    if so, it's better to exchange so record that!
    3. also consider dollar where you dont add +1
'''
def calcExactCost(d, cost):
    cost[0]=0
    for i in xrange(1, maxN):
        if(cost[i] == float('inf')): 
            minList = []
            for index in xrange(len(d)):
                if i-d[index] > 0 and cost[(i-d[index])]!=0:
                    minList += [cost[(i-d[index])] ]
            if minList == []: cost[i] = 0
            else: cost[i] = 1+ min(minList)
    #print cost
    return cost

def calcExchangeCost(exactCost, denom):
    exchangeCost = [-1]*maxN
    for i in xrange(1, maxN):
        bestExchangeCost = exactCost[i]#is exact cost to start with
        #get list of denom that's bigger than me, add dollar at index 0 default
        listOfChanges=[100-i]
        for d in denom:
            if d>i:
                listOfChanges+=[i-d]
        for c in range(len(listOfChanges)):
            change = listOfChanges[c]
            #but if exactCost[change] == 0, that means that part 
            #couldn't be calculated because of a loss of penny, so do not add to min comparison
            if exactCost[change]>0:
                if c is 0: exactCostForAChange = exactCost[change] #this is a dollar
                else: exactCostForAChange = exactCost[change]+1
                if bestExchangeCost >0:
                    if exactCostForAChange < bestExchangeCost:
                        bestExchangeCost = exactCostForAChange
                else: bestExchangeCost = exactCostForAChange
        exchangeCost[i] = bestExchangeCost
    return exchangeCost
    
def initCost(denom):
    cost = [float('inf')] * maxN
    for i in xrange(len(denom)):
        cost[denom[i]]=1
    return cost


def nextBestExchange(lastWinner):
    global counter
    bestScore = (float('inf'), float('inf'))
    bestCost = []
    bestSoFar = []
    for i in xrange(1, maxN/2):
        if(i not in lastWinner):
            tryDenom = lastWinner+[i]
            cost = initCost(tryDenom)
            counter += 1
            exactCost = calcExactCost(tryDenom, cost)
            exchangeCost = calcExchangeCost(exactCost, tryDenom)
            if 0 not in exchangeCost:
                print "for ", tryDenom
                #print "0 haitte nai", exchangeCost
                result =winner.getAvgCost(exchangeCost)
                if result[0] < bestScore[0]:
                    bestScore = result
                    bestSoFar = tryDenom
                    bestCost = exchangeCost
                    print "bestCost!! %s" % bestCost
    print "With N=%s and %s denom, the best score is: %s with avg # of coins:%s with denomination: %s" %(n, len(lastWinner)+1, bestScore[0], bestScore[1],bestSoFar)
    print "With best cost %s"%bestCost
    return (bestSoFar, bestScore)

def tryExchange(arg1):
    global counter, n
    n = arg1
    counter = 0
    maxN= 100
    bestScore = (float('inf'), float('inf'))
    bestCost = []
    bestSoFar = []
    for i in range(1, maxN/2-4):
        for j in range(i+1, maxN/2-3):
            for h in range(j*2, maxN/2-2):
                for k in range(h*2, maxN/2-1):
                    for g in range(k*2, maxN/2):
                        tryDenom = [i,j,h,k, g]
                        cost = initCost(tryDenom)
                        exactCost = calcExactCost(tryDenom, cost)
                        exchangeCost = calcExchangeCost(exactCost, tryDenom)
                        if 0 not in exchangeCost:
                            #print "for ", tryDenom
                            #print "0 haitte nai", exchangeCost
                            result =winner.getAvgCost(exchangeCost)
                            if result[0] < bestScore[0]:
                                bestScore = result
                                bestSoFar = tryDenom
                                bestCost = exchangeCost
                                #print "bestCost!! %s" % bestCost
    print "With N=%s and best FOR EXCHANGE is %s with score: %s with avg # of coins:%s" %(n, bestSoFar, bestScore[0], bestScore[1])
    #print "With best cost %s"%bestCost
#    bestOne = nextBestExchange([])
#    bestTwo= nextBestExchange(bestOne[0])
#    bestThree = nextBestExchange(bestTwo[0])
#    bestFour = nextBestExchange(bestThree[0])
#    bestFive = nextBestExchange(bestFour[0])
#
#    print "With N=%s the best denom  for EXCHANGE is %s with score:%s, avg:%s"%(n, bestFive[0], bestFive[1][0], bestFive[1][1])
#    print "Looked at %s denominations" % counter
 
if __name__ == '__main__':
    global n
    n = sys.argv[1]
    start = time.clock()
    tryExchange(n)
    print "It took", (time.clock()-start),"seconds to complete"
    print "now:", time.clock(), "start:", start