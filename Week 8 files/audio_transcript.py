import json
import sys
import csv

if not (len(sys.argv) == 2):
    print("Usage: {} json_file".format(sys.argv[0]))
    exit()

with open(sys.argv[1]) as json_file:  
    data = json.load(json_file)

# per shot information
text = data['response']['results']
out = []
for piece in text:
    confidence = float(piece['alternatives'][0]['confidence'])
    if confidence < 0.80: 
        out.append("[" + piece['alternatives'][0]['transcript'] + "]")
    else:
        out.append(piece['alternatives'][0]['transcript'])

# join the data together
print(" ".join(out))