namematch.py
=========
2013-03-11 by Ben Wheeler wheeler.benjamin@gmail.com for Knewton

written in python3.3, first line assumes a dir containing the executable python3 is in the user's PATH. 

BANDLISTFILENAME is a (i'm quoting from the assignment text here)
utf-8 encoded text file that contains the favorite musical artists of 1000
users from LastFM. Each line is a list of up to 50 artists, separated by commas. 

usage: 
namematch.py -f BANDLISTFILENAME [-t NUMTIMESTHRESH, defaults to 50]

output:
Oasis,The Killers
...
<<EOF

efficiency: 
=========
assuming that there are n lines with approx k bands each:
runtime: O(k^2 * n)
since we have an upper bound of 50 for k, we can simplify this to 
O(n)
i imagine that in practice, much of my code's runtime is spent in resizing the main 
dict as it grows, and waiting on OS page requests. 

storage: worst case O(k^2 * n), which again we can simplify to O(n) since we have an upper bound for k. 
the typical case depends on the degree of overlap in user lists. 
that could be empirically determined. i would expect something more like O(log n). 




