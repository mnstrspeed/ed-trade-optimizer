import json
import math
import difflib
from layout import *

stations = json.load(open('merged_stations.json'))
commodities = json.load(open('commodities.json'))

print "Loaded {} stations and {} commodities".format(len(stations), len(commodities))

excluded_commodities = [c['id'] for c in commodities if c['name'] in \
    ['Imperial Slaves', 'Slaves', 'Superconductors']]

def distance(a, b):
    dx = a["x"] - b["x"]
    dy = a["y"] - b["y"]
    dz = a["z"] - b["z"]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def profit((a, b)):
    if a == None or b == None:
        return 0
    return b["sell_price"] - a["buy_price"]

def best_deal(a, b):
    deals = [(al, bl) for al in a["listings"] for bl in b["listings"] if \
        al["commodity_id"] == bl["commodity_id"] and \
        al["commodity_id"] not in excluded_commodities and \
        al["supply"] > 0 and bl["demand"] > 0 and \
        al["buy_price"] > 0 and bl["sell_price"] > 0]
    if not deals:
        return (None, None)
    return max(deals, key=profit)

def station(name):
    return next(s for s in stations if s['name'] == name)

print "station(name)"
print "best_deal(station_a, station_b)"
print "profit(listing_a, listing_b)"

