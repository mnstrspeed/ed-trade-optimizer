# ed-trade-optimizer
Trade helper for Elite: Dangerous that searches for a trade route `a -> b` that maximizes `profit(best_deal(a, b)) + profit(best_deal(b, a))` 

Currently required 3 steps:
1. Download the latest `stations.json`, `systems.json`, and `commodities.json` from http://eddb.io/api
2. Run `merge.py` to optimize the data set for trade calculations
3. Run `route.py` to search for optimal trade routes

The search algorithm starts off in a source system (specific by the user) and gradually expands the search space. Better routes are reported as they are found, so optimal route profits increases with longer running times of the program (although these routes will also be further from the source).

## Sample output
```
            LP 751-1   ────────────────────────────Gold────────────────────────────╮  V1688 Aquilae
        Tito Orbital  1013 profit            40.134807018 Ly            1302 profit   Eanes Gateway
            (168 Ls)  ╰───────────────────────Battle Weapons───────────────────────   (192 Ls)     
                                                                                                    

              Trella   ─────────────────────────Palladium──────────────────────────╮  LTT 7548         
         Tito Colony  1324 profit            38.365583128 Ly            1083 profit   Boltzmann Gateway
            (812 Ls)  ╰───────────────────Resonating Separators────────────────────   (1001 Ls)        
                                                                                                        

               Brani   ─────────────────────────Palladium──────────────────────────╮  LTT 7548         
        Virtanen Hub  1552 profit            39.1619608764 Ly            894 profit   Boltzmann Gateway
             (16 Ls)  ╰────────────────────Consumer Technology─────────────────────   (1001 Ls) 
```
