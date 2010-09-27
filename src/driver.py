'''
Created on Sep 27, 2010

@author: ajk377
'''
import sys, time, exchange, winner

if __name__ == '__main__':
    global n
    n = sys.argv[1]
    start = time.clock()
    winner.tryAll(n)
    exchange.tryExchange(n)
    print "It took", (time.clock()-start),"seconds to complete"
    print "now:", time.clock(), "start:", start