import sys
import png

def add_to_results(val):
    global maxval
    if val > maxval:
        maxval = val
    results.append(val)

def image_generator():
    for i in range(yResolution, 0, -1):
        for x in results:
            if x >= i: 
                yield fgColor[0]
                yield fgColor[1]
                yield fgColor[2]
                yield fgColor[3]
            else:
                yield bgColor[0]
                yield bgColor[1]
                yield bgColor[2]
                yield bgColor[3]

in_filename = sys.argv[1]
out_filename = sys.argv[2]

first = None
last  = None

fgColor = (255, 0, 0, 255)
bgColor = (255, 255, 255, 0)

infile = open(in_filename, "r")
maxval = 0

yResolution = 100
ptsPerPixel = 10000
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

    while currStart + ptsPerPixel < start:
        add_to_results(float(currTotal)/ptsPerPixel)
        
        currTotal = 0
        currStart += ptsPerPixel

    if currStart + ptsPerPixel > end:
        currTotal += (end-start)*value
    else:
        currTotal += (currStart+ptsPerPixel-start)*value
        add_to_results(float(currTotal)/ptsPerPixel)

        currTotal = (end-currStart-ptsPerPixel)*value
        currStart = end

results.append(float(currTotal)/(last-currStart))

infile.close()

results = map(lambda x: yResolution*x/maxval, results)

w = png.Writer(len(results), yResolution, alpha = True)
outfile = open(out_filename, "wb")
w.write_array(outfile, list(image_generator()))
outfile.close()

# print results
