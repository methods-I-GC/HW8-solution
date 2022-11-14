#!/usr/bin/env python
"""Randomly shuffles a file by lines."""

import argparse
import random


def main(args: argparse.Namespace) -> None:
    data = []
    with open(args.input, "r") as source:
        for line in source:
            data.append(line.rstrip())
    random.seed(args.seed)
    random.shuffle(data)
    with open(args.output, "w") as sink:
       for line in data:
            print(line, file=sink) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="output file path")
    parser.add_argument("--seed", type=int, required=True, help="random seed")
    main(parser.parse_args())
