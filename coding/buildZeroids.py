import random
import string
#loc = random.randint(0,2000)
loc = 1225
SECRET = "A1cerberus\n"
          


out = []
for x in range(2000):
    theText = "".join([random.choice(string.ascii_letters) for x in range(10)])
    out.append("{0}\n".format(theText))
    if x == 1242:
        out.append(SECRET)

fd = open("hydra.txt","w")
fd.writelines(out)
fd.close()



