#!/usr/bin/python3


def main():
    from sys import argv
    argument = "arguments"
    punc = "."
    print("{0} {1}{2}".format(len(argv[1:]), argument, punc))
    for k, v in enumerate(argv[1:], start=1):
        print("{0}: {1}".format(k, v))
if (__name__ == '__main__'):
    main()
