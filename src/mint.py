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

n=0;

def calcCost(cost):
    for i in range(2, 100):
        if cost[i]==1e308:
#            print "at i:", i
            for j in range(1, i):
             #   print "looking at j:",j,"i-j: ", (i-j)," cost[j]=", cost[j], " cost[i-j]=", cost[i-j]," cost[i]=", cost[i]
                if(cost[j]+cost[i-j] < cost[i]):
                    cost[i]=cost[j]+cost[i-j]
              #      print "cost[",i,"] is now ", cost[i]
    return 0

def getAvgCost(cost):
    total = score=0.0
    for i in range(1, 100):
        total+= cost[i]
   #     print "# of coins for ", i," is ", cost[i];
        if cost[i] % 5 is 0:
            score+=cost[i]*n
        else:
            score+=cost[i]
    print "total:",total,"avg cost:",(total/99) ,"\n score: ", score;
    return (score, total/99);
'''
    Eliminating search space:
        given an upper bound, B, which the highest # of coins needed to pay
        any amount from 1-99cent, you must have a coin at least total/B.
        i.e. if B = 4, your denomination must have 25. 
        i.e. if max{denom}<25, useless.
        Say B = 5, you must have a 20
'''
def tryAll():
    bestQuad = [1, 2, 3, 4, 5];
    best = (1e308, 0);
    cost = [1e308]*100;
    upperBound = math.ceil(99.0/5);
    for i in range(2, 97):
      #  cost[i:] = [1e308]*(100-i) #reuse the lookup table
        for j in range(i+1, 98):
       #     cost[j:]=[1e308]*(100-j)
            for h in range(j+1, 99):
        #        cost[h:]=[1e308]*(100-h)
                for k in range(h+1, 100):
         #           cost[k:]=[1e308]*(100-k)
                    cost = [1e308]*100;
                    tryQuad = [1, i, j, h, k];
                    if max(tryQuad)>=upperBound:
                        cost[1]=cost[i]=cost[j]=cost[h]=cost[k]=1;
                        calcCost(cost)
                        print "for ", tryQuad
                        result = getAvgCost(cost)
                        if result[0] < best[0]:
                            best = result
                            bestQuad = tryQuad
    print "the best score is: ", best[0], " with avg # of coins:", best[1]," with denomination: " ,bestQuad
    
def main():
 #   n = raw_input("What's the N?")
    n = sys.argv[1]
    print "With N="+ n
    start = time.clock()
    tryAll()
    print "It took", (start-time.clock())," to complete"
 
    
if __name__ == '__main__':
    main();
    