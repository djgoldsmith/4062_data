import random
import string
#loc = random.randint(0,2000)
loc = 1725
SECRET = "adMOIDS_or_ZErOiDSs\n"
          


out = []
for x in range(2000):
    theText = "".join([random.choice(string.ascii_letters) for x in range(20)])
    out.append("{0}\n".format(theText))
    if x == 1242:
        out.append(SECRET)

fd = open("zeroids.txt","w")
fd.writelines(out)
fd.close()



