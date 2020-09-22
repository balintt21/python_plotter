#!/usr/bin/env python3

import os
import sys
import json
import errno
import matplotlib.pyplot as plt


def main():
    if len(sys.argv) < 2 or ("-h" in sys.argv) or ("--help" in sys.argv):
        print(f"Usage: {sys.argv[0]} <json_file_path|text:json|text:python array>")
        print("Input:\n\ttext:json\n\t\t{ \"x\": [1,2,3,...], \"y\": [1,2,3,...] }\n\ttext:python array\n\t\t[1,2,3,...]\n")
        exit(0)
    
    data = []
    arg = sys.argv[1]
    if os.path.isfile(arg):
        with open(arg, "r") as file:
            data = json.load(file)
    else:
        data = json.loads(arg)
    
    if isinstance(data, list):
        plt.plot(data)
    elif isinstance(data,dict) and ("x" in data) and ("y" in data):
        plt.plot(data["x"], data["y"])
    else:
        exit(errno.EINVAL)
    plt.show()

if __name__ == "__main__":
    main()
