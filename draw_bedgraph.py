import sys

in_filename = sys.argv[1]
# out_filename = sys.argv[2]

first = None
last  = None

infile = open(in_filename, "r")
maxval = 0

resolution = 10000
results = []
currTotal  = 0
currStart  = None

lineno = 0

for line in infile:
    lineno += 1
    toks = line.split()
    start = int(toks[1])
    end   = int(toks[2])
    value = int(toks[3])

    if first == None:
        first = start

    if currStart == None:
        currStart = start
        
    curr = start
    last = end

    if value > maxval:
        maxval = value

    while currStart + resolution < start:
        results.append(currTotal)
        currTotal = 0
        currStart += resolution

    if currStart + resolution > end:
        currTotal += (end-start)*value
    else:
        currTotal += (currStart+resolution-start)*value
        results.append(currTotal)

        currTotal = (end-currStart-resolution)*value
        currStart = end

results.append(currTotal)

infile.close()

