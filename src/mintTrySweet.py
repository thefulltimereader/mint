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

maxN = 161;
cost = []
def calcCost(i, d):
    if(cost[i]!= float('inf')): return cost[i]
    else:
        minList = []
        for index in range(len(d)):
            if i-d[index] > 0:
                minList += [calcCost(i-d[index], d)] 
        cost[i] = 1+ min(minList)
        return cost[i] 
    #print cost
    
def calcCostOld(cost):
    for i in range(2, maxN):
        if cost[i]==float('inf'):
            for j in range(1, i):
                #print "looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                if(cost[j]+cost[i-j] < cost[i]):
                    cost[i]=cost[j]+cost[i-j]
                  #  print "at i: ",i," looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                  #  print "cost[",i,"] is now ", cost[i]
    #print cost
    
def calcAll(i, d):
    for index in range(1, maxN):
        if cost[index]==float('inf'):
            calcCost(index, d)
        

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
        given an upper bound, B, which the highest # of coins needed to pay
        any amount from 1-99cent, you must have a coin at least total/B.
        i.e. if B = 4, your denomination must have 25. 
        i.e. if maxN{denom}<25, useless.
        Say B = 5, you must have a 20
'''
def tryAll(n):
    bestQuad = [1, 2, 3, 4];
    best = (float('inf'), float('inf'));
    global cost
    cost = [float('inf')]*maxN
    upperBound = math.ceil(float(maxN-1)/5);
    for i in range(2, maxN-30):
        for j in range(i*2, maxN-20):
            cost[i:]=[float('inf')]*(maxN-i)#reuse the lookup table
            for h in range(j*3, maxN-10):
                cost[j:]=[float('inf')]*(maxN-j)
               # cost = [float('inf')]*maxN
                tryQuad = [1, i, j, h];
                if max(tryQuad)>=upperBound:
                        cost[1]=cost[i]=cost[j]=cost[h]=1;
                        calcAll(maxN-1, tryQuad)
                        #calcCostOld(cost)
                        print "for ", tryQuad
                        result = getAvgCost(cost, n)
                        if result[1] < best[1]:
                            best = result
                            bestQuad = tryQuad
                            print "better:", cost

    print "With N=", n,"the best score is: ", best[0], " with avg # of coins:", best[1]," with denomination: " ,bestQuad
    
def exchange():
    return 0
def main():
 #   n = raw_input("What's the N?")
    n = sys.argv[1]
    start = time.clock()
    tryAll(n)
    print "It took", (time.clock()-start),"seconds to complete"
 
    
if __name__ == '__main__':
    main();
    