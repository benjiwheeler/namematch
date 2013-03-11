#!/usr/bin/env python3

import csv
with open('Artist_lists_small.txt', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    togetherInstances = dict()
    for row in csvreader:
        already = set()
        for band in row:
            #print("%s, " % (band), end="")
            for alreadyband in already:
                if band < alreadyband:
                    alpha = band
                    beta = alreadyband
                else:
                    alpha = alreadyband
                    beta = band
                #print("pairing %s with %s" % (alpha, beta))
                if (alpha, beta) in togetherInstances:
                    togetherInstances[(alpha, beta)] += 1
                    #print("already there, %d times total" % togetherInstances[(alpha, beta)])
                else:
                    togetherInstances[(alpha, beta)] = 1
            already.add(band)

    for (alpha, beta), numtimes in togetherInstances.items():
        if numtimes >= 50:
            print("%s and %s appeared together %d times" % (alpha, beta, numtimes))



