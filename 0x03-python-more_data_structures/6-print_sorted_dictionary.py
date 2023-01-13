#!/usr/bin/pythone3


def print_sorted_dictionary(richard):
    for k in sorted(richard):
        print("{0}: {1}".format(k, richard.get(k)))
