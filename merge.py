#! /usr/bin/python

import json
import msgpack
import time
import sys

def progress(l):
    start_time = time.time()
    print ".../... (...%)",
    for i, x in enumerate(l):
        if time.time() > start_time + 1.0:
            start_time = time.time()
            print "\r{}/{} ({}%)".format(i, len(l), (i * 100) / len(l)),
            sys.stdout.flush()
        yield x

print "Reading data..."
systems = json.load(open('systems.json'))
stations = json.load(open('stations.json'))

print "Merging data..."
for station in progress(stations):
    system = [s for s in systems if s["id"] == station["system_id"]][0]
    
    station["system_name"] = system["name"]
    station["x"] = system["x"]
    station["y"] = system["y"]
    station["z"] = system["z"]

print "Saving to merged_stations.json..."
with open('merged_stations.mp', 'w') as out:
    msgpack.pack(stations, out)
print "Done"
