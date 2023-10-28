"""
CMSC 14100
Aut 23

Functions for reading shakespeare lines from JSON files

"""

import json
import sys
import os

def load_sample(filename):
    """ 
    Load a sample of play lines from a JSON file

    Input:
        filename (str): name of JSON file to load
    
    Returns:
        List[Dict[Str, Any]]: list of lines from the play
    """
    try:
        if not filename.endswith(".json"):
            print("Wrong file type. This function only loads JSON files\n")
            sys.exit(1)
        f = os.path.exists(filename)
        data = None
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return data

    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    