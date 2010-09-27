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

maxN = 100;
cost = []
flag=False
def calcCost(d):
    cost[0]=0
    for i in xrange(1, maxN):
        if(cost[i] == float('inf')): 
            minList = []
            for index in xrange(len(d)):
                if i-d[index] > 0:
                    minList += [cost[(i-d[index])] ]
            cost[i] = 1+ min(minList)
    print cost
    
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
def getAvgCost(cost, n):
    total = score=0.0
    for i in range(1, maxN):
        total+= cost[i]
   #     print "# of coins for ", i," is ", cost[i];
        if i % 5 is 0:
            score+=cost[i]*float(n)
        else:
            score+=cost[i]
    print "total:",total,"avg cost:",(total/maxN-1) ,"\n score: ", score;
    return (score, (total/maxN-1));
'''
    Eliminating search space:
     A: given an upper bound, B, which the highest # of coins needed to pay
        any amount from 1-99cent, you must have a coin at least total/B.
        i.e. if B = 4, your denomination must have 25. 
        i.e. if maxN{denom}<25, useless.
        Say B = 5, you must have a 20
     B: Who needs [1,2,3,4,9], or [1,2,3,4,99]?. Given d=[d1,d2,d3,d4,d5]
        Esp the distance bewteen d4, d5 should be big enough.
        Idea of Fast foward: when evaluating every x for [d1,d2,d3,d4,x]. If
        [d1,d2,d3,d4,x-1] does not do well, instead of incrementing  by 1, 
        fast forward. It's probably not because of the x, but the set [d1,d2,d3,d4]
        What is "not doing well"? have a running avg score so far, if that set 
        [d1,d2,d3,d4] does not go above the running avg, fast forward
      C: Do we need any coin bigger than .50??  Say there exists d5=.75, it is 
        good for the last quarter of a dollar, we can use the first quarter to calculate the last quarter,
        but if 50cent coin allows us to use half of to copy over to the second half.
        i.e. with 75cent, you can copy the first 1/4, to the last 1/4 with all val +1
        with 50cent, you can copy the first 1/2 to the last 1/2 with all val +1, 
        50cent is much more space efficient 
'''
def tryAll(n):
    bestQuad = [1, 2, 3, 4, 5]; best = (float('inf'), float('inf'));
    bestCost=[float('inf')]*maxN
    runningAvg = counter =0
    global cost
    cost = [float('inf')]*maxN
    upperBound = maxN/5;
    for i in range(2, maxN/2-3):
        for j in range(i+1, maxN/2-2):
            for h in range(j+1, maxN/2-1):
                for k in range(h+1, maxN/2):
                    cost = [float('inf')]*maxN
                    tryQuad = [1, i, j, h, k]
                    if max(tryQuad)>=upperBound:
                        cost[1]=cost[i]=cost[j]=cost[h]=cost[k]=1;
                        counter+=1
                        #calcCost(tryQuad)
                        calcCostOld(cost)
                        print "for ", tryQuad
                        result = getAvgCost(cost, n)
                        if result[0] < best[0]:
                            best = result
                            bestQuad = tryQuad
                            bestCost = cost
                            print "bestCost!! %s"%bestCost
                            
    print "With N=", n,"the best score is: ", best[0], " with avg # of coins:", best[1]," with denomination: " ,bestQuad
    print "With best cost %s"%bestCost
    print "Looked at %s denominations" % counter
def main():
 #   n = raw_input("What's the N?")
    n = sys.argv[1]
    start = time.clock()
    tryAll(n)
    print "It took", (time.clock()-start),"seconds to complete"
    print "now:", time.clock(), "start:", start
 
    
if __name__ == '__main__':
    main();
    