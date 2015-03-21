# ed-trade-optimizer
Trade helper for Elite: Dangerous that searches for a trade route `a -> b` that maximizes `profit(best_deal(a, b)) + profit(best_deal(b, a))` 

Currently required 3 steps:
1. Download the latest `stations.json`, `systems.json`, and `commodities.json` from http://eddb.io/api
2. Run `merge.py` to optimize the data set for trade calculations
3. Run `route.py` to search for optimal trade routes

The search algorithm starts off in a source system (specific by the user) and gradually expands the search space. Better routes are reported as they are found, so optimal route profits increases with longer running times of the program (although these routes will also be further from the source).
