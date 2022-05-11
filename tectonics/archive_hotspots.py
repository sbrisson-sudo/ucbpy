#!/usr/bin/env python

import json
import pickle
import numpy as np

def main():
    with open('hotspots.json', 'r') as f:
        hotspots = json.load(f)
        
    hs_names = list(hotspots.keys())
    hs_values = np.array(hotspots.values())
    
    with open('hotspots.pkl', 'wb') as f:
        pickle.dump((hs_names, hs_values), f)

if __name__ == '__main__':
    main()
