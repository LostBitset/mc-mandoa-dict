import json

from make_entry import make_entry

dat = None
with open("capture.json", "r") as f:
    dat = json.load(f)

dictionary = [ make_entry(i) for i in dat ]
print(dictionary[1])

