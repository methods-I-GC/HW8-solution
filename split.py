#!/usr/bin/env python
"""Randomly splits a file by lines into three sets."""

import argparse
import random


def main(args: argparse.Namespace) -> None:
    data = []
    with open(args.input, "r") as source:
        for line in source:
            data.append(line.rstrip())
    random.seed(args.seed)
    random.shuffle(data)
    ten_pct = len(data) // 10
    eighty_pct = 8 * ten_pct
    ninety_pct = eighty_pct + ten_pct
    with open(args.train, "w") as sink:
       for line in data[:eighty_pct]:
            print(line, file=sink)
    with open(args.dev, "w") as sink:
        for line in data[eighty_pct:ninety_pct]:
            print(line, file=sink)
    with open(args.test, "w") as sink:
        for line in data[ninety_pct:]:
            print(line, file=sink)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("train", help="output training file path")
    parser.add_argument("dev", help="output development file path")
    parser.add_argument("test", help="output test file path")
    parser.add_argument("--seed", type=int, required=True, help="random seed")
    main(parser.parse_args())
