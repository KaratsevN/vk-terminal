import os
from src.size import ConsoleSize
# lol = os.popen('stty size', 'r').read().split()
# print(lol)


def main():
    size = ConsoleSize()
    rows, columns = size.getSize()
    print({},{}).format(size.getSize())
main()