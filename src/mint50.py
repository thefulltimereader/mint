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

'cost = [1e308]*100;'
import time, math, sys

maxN = 50;

def calcCost(cost):
    for i in range(2, maxN):
        if cost[i]==1e308:
            for j in range(1, i):
                #print "looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                if(cost[j]+cost[i-j] < cost[i]):
                    cost[i]=cost[j]+cost[i-j]
                  #  print "at i: ",i," looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                  #  print "cost[",i,"] is now ", cost[i]
    #print cost

def getAvgCost(cost, n):
    total = score=0.0
    for i in range(1, maxN):
        total+= cost[i]
   #     print "# of coins for ", i," is ", cost[i];
        if i % 5 is 0:
            score+=cost[i]*float(n)
        else:
            score+=cost[i]
    print "total:",total,"avg cost:",(total/99) ,"\n score: ", score;
    return (score, (total/99));
'''
    Eliminating search space:
        given an upper bound, B, which the highest # of coins needed to pay
        any amount from 1-99cent, you must have a coin at least total/B.
        i.e. if B = 4, your denomination must have 25. 
        i.e. if maxN{denom}<25, useless.
        Say B = 5, you must have a 20
'''
def tryAll(n):
    bestQuad = [1, 2, 3, 4, 5];
    best = (1e308, 0);
    cost = [1e308]*maxN
    upperBound = math.ceil(float(maxN-1)/5);
    for i in range(2, maxN-30):
        cost[i:] = [1e308]*(maxN-i) #reuse the lookup table
        for j in range(i+1, maxN-20):
            cost[j:]=[1e308]*(maxN-j)
            for h in range(j+1, maxN-10):
                cost[h:]=[1e308]*(maxN-h)
                for k in range(h+1, maxN):
                    cost[k:]=[1e308]*(maxN-k)
                    #cost = [1e308]*maxN
                    tryQuad = [1, i, j, h, k];
                    if max(tryQuad)>=upperBound:
                        cost[1]=cost[i]=cost[j]=cost[h]=cost[k]=1;
                        calcCost(cost)
                        print "for ", tryQuad
                        result = getAvgCost(cost, n)
                        if result[0] < best[0]:
                            best = result
                            bestQuad = tryQuad
                            print "better:", cost

    print "With N=", n,"the best score is: ", best[0], " with avg # of coins:", best[1]," with denomination: " ,bestQuad
    
def main():
 #   n = raw_input("What's the N?")
    n = sys.argv[1]
    start = time.clock()
    tryAll(n)
    print "It took", (time.clock()-start),"seconds to complete"
    print "now:", time.clock(), "start:", start
 
    
if __name__ == '__main__':
    main();
    