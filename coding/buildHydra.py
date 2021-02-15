fd = open("Hydra.txt","r")

#data = fd.readlines()
#print(len(data))
#for line in data:
#  print line

import base64

out = []
idx = 1
for line in fd:
  theStr = "{0:03d} {1}".format(idx, line)
  out.append('echo {0} | base64 -d\n'.format(base64.b64encode(theStr.encode()).decode()))
  idx += 1

#for x in range(5):
#  print(out[x])

import random

rout = random.shuffle(out)
print (out[0:5])

outfd = open("Shadows.txt","w")
outfd.writelines(out)
outfd.close()

