import json
import sys
import csv

if not (len(sys.argv) == 2):
    print("Usage: {} json_file".format(sys.argv[0]))
    exit()

with open(sys.argv[1]) as json_file:  
    data = json.load(json_file)

# per shot information
shot_data = data['annotationResults'][0]['shotLabelAnnotations']
out = []
for shot_datum in shot_data:
    if 'categoryEntities' in shot_datum:
        category = shot_datum['categoryEntities'][0]["description"]
    else:
        category = None
    entity = shot_datum['entity']["description"]
    segments_raw = shot_datum["segments"]
    for segment_raw in segments_raw:
        start_time = segment_raw['segment']['startTimeOffset'][:-1]
        end_time = segment_raw['segment']['endTimeOffset'][:-1]
        confidence = "{:.0f}%".format(float(segment_raw['confidence'])*100)
        out.append([category, entity, start_time, end_time, confidence])

# write out in csv format
writer = csv.writer(sys.stdout)
headings = ["Category", "Item", "Start time (s)", "End time (s)", "Confidence"]
writer.writerow(headings)
for row in out: 
    writer.writerow(row)