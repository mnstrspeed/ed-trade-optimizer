import json
import msgpack
import math
import difflib
from layout import *

#stations = json.load(open('merged_stations.json'))
stations = msgpack.unpack(open('merged_stations.mp'))
commodities = json.load(open('commodities.json'))

print "Loaded {} stations and {} commodities".format(len(stations), len(commodities))

location = None
while not location:
    query = raw_input('Where are you? [Worlidge Station] ')
    if not query:
        location = next(x for x in stations if x['name'] == "Worlidge Terminal")
    else:
        matches = difflib.get_close_matches(query, \
            [s['name'] for s in stations])
        for i, match in enumerate(matches):
            s = next(s for s in stations if s['name'] == matches[i])
            print "{}. {}, {}".format(i, s['name'], s['system_name'])
        selected = raw_input('Index: ')
        if 0 <= int(selected) < len(matches):
            location = next(x for x in stations if x['name'] == matches[int(selected)])

def distance(a, b):
    dx = a["x"] - b["x"]
    dy = a["y"] - b["y"]
    dz = a["z"] - b["z"]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

nearby = sorted(stations, key=lambda x: distance(location, x))
nearby = filter(lambda s: 0 < s['distance_to_star'] < 5000, nearby)
excluded_commodities = [c['id'] for c in commodities if c['name'] in \
    ['Imperial Slaves', 'Slaves', 'Superconductors']]

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

def commodity(x):
    return [c for c in commodities if c["id"] == x["commodity_id"]][0]
def print_route(r):
    borders = (' ', u'\u256e', u'\u2570', ' ')
    lines = column([
        [ r['a']['system_name'], r['a']['name'], "({} Ls)".format(r['a']['distance_to_star']), left(width=20) ],
        [
            borders[0] + line(60, commodity(r['ab'][0])['name']) + borders[1],
            "".join(column([ \
                ["{} profit".format(profit(r['ba']))], \
                ["{} Ly".format(distance(r['a'], r['b']))], \
                ["{} profit".format(profit(r['ab']))]], width=62)),
            borders[2] + line(60, commodity(r['ba'][0])['name']) + borders[3]
        ],
        [ r['b']['system_name'], r['b']['name'], "({} Ls)".format(r['b']['distance_to_star']) ],
    ], align=[right, left, left], separator='  ')
    print '\n'.join(lines), '\n'

best = { 'value': 0 }
processed = []
for a in nearby:
    for b in processed:
        entry = { 'a': a, 'b': b }
        entry['ab'] = best_deal(a, b)
        entry['ba'] = best_deal(b, a)
        entry['value'] = profit(entry['ab']) + profit(entry['ba'])
        if entry['value'] > best['value']:
            print_route(entry)
            best = entry
    processed.append(a)
routes.sort(key=lambda entry: entry['value'], reverse=True)
