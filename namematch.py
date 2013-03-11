#!/usr/bin/env python3
# i use python 3.3 when i can, but i think the code below should run on 2.7 with only slight changes

import csv
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="bandListFilename", required=True)
parser.add_argument("-t", dest="numTimesThresh", type=int, required=False, default=50)
args = parser.parse_args()

# counts number of times two bands appear on a single-line list together.
# internal representation is:
# key: tuple of two alphabetized band names
# value: number of times encountered (zero if key not present)
togetherInstances = dict()
# provides quick access to set of pairs that meet thresh
pairsMeetingThresh = set()

try:
    # open csv file and iterate through its rows and within each row.
    # note that encoding might not be being handled correctly; there
    # are some strange character sequences that might not have utf-8
    # encodings
    with open(args.bandListFilename, 'r', encoding="UTF-8") as csvfile:
        # note that input file may have line break issues; there are
        # lines that appear to repeat band names
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            # init empty set to use on this row: track bands already
            # iterated over on this row. the only pairs we consider
            # are current band at the iterator, and previous bands we
            # have seen earlier on the line.
            bandsAlreadySeenInThisRow = set()
            # init empty dict to use on this row: helps us catch when
            # we might double count a pair that erroneously appears
            # more than once on a single line
            pairsAlreadySeenInThisRow = dict()

            for band in row:
                for bandAlreadySeen in bandsAlreadySeenInThisRow:

                    # order current band and band already seen alphabetically
                    alpha = bandAlreadySeen
                    omega = band
                    if band < bandAlreadySeen:
                        alpha = band
                        omega = bandAlreadySeen

                    # make sure we have not counted this pair already on this row
                    if (alpha, omega) in pairsAlreadySeenInThisRow:
                        print("Warning: a row has an unexpected duplicate (%s and %s)" 
                              % (band, bandAlreadySeen))
                        next
                    pairsAlreadySeenInThisRow[(alpha, omega)] = True

                    # count the pair as a new instance
                    if (alpha, omega) in togetherInstances:
                        togetherInstances[(alpha, omega)] += 1
                        if togetherInstances[(alpha, omega)] >= args.numTimesThresh:
                            pairsMeetingThresh.add((alpha, omega))
                    else:
                        togetherInstances[(alpha, omega)] = 1

                bandsAlreadySeenInThisRow.add(band)

except:
    print("Failed to correctly process file %s" % args.bandListFilename)
    sys.exit(1)

try:
    for (alpha, omega) in pairsMeetingThresh:
        print("%s,%s" % (alpha, omega))
except TypeError:
    print("Error: numTimesThresh arg must be an integer")
    sys.exit(1)


