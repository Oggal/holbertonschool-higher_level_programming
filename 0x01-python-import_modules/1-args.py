#!/usr/bin/python3


def main():
    from sys import argv
    myArg = argv[1:]
    argument = "arguments"
    if (len(myArg) == 1):
        argument = "argument"
    punc = "."
    if (len(myArg) == 1):
        punc = ":"
    print("{0} {1}{2}".format(len(myArg), argument, punc))
    for k, v in enumerate(myArg, start=1):
        print("{0}: {1}".format(k, v))
if (__name__ == '__main__'):
    main()
