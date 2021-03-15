import base64

FILENAME = "../ascii_art/dino_ascii.txt"
OUTFILE = "target.sh"

outArray = []

idx = 0 
with open(FILENAME,"r") as fd:
    for line in fd:
        theStr = "{0} {1}".format(idx, line)
        encoded = base64.b64encode(theStr.encode()).decode()
        outArray.append("echo {0} | base64 -d".format(encoded))

        idx +=1

outArray.append("echo '\n'")        

for line in outArray:
    print(line)
