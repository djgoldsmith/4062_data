import base64

FILENAME = "../ascii_art/games_can_kill.txt"
OUTFILE = "target.sh"

outArray = ["echo '\n'"]

idx = 1000
with open(FILENAME,"r") as fd:
    for line in fd:
        theStr = "{0} {1}".format(idx, line)
        encoded = base64.b64encode(theStr.encode()).decode()
        outArray.append("echo {0} | base64 -d".format(encoded))

        idx -=1

#outArray.reverse()
import random
random.shuffle(outArray)

for item in outArray:
    print(item)


