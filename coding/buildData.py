import json
import random
import string

STRLEN = 10

flag = "CUEH{PyFlag}"

data = {}
checksum = []
names = ["dan", "james", "terry", "tono", "john","fred","barney","wilma","pebbles","betty","bambam","xiang"]

import pprint

for idx, item in enumerate(names):
    print("X {} N {}".format(idx, item))

    #Some random values
    values = [random.randrange(10) for x in range(5)]
    total = sum(values)

    #Take the first of our random values and make it the checksum
    selected = values[0]
    checksum.append(selected)

    theText = [random.choice(string.ascii_letters) for x in range(STRLEN)]

    theText[selected] = flag[idx]

    theUser = {"name": item,
               "values": values,
               "total": total,
               "text": "".join(theText)
    }

    data[idx] = theUser
    #pprint.pprint(theUser)


output = {"dataset" : "testdata",
          "checksum": checksum,
          "data": data
        }


with open("testdata.json", "w") as fd:
    #out = json.dump(output, fd, sort_keys=True, indent=4)
    out = json.dump(output, fd)

