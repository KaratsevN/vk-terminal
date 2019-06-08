import os
from src.interface.size import Size
# lol = os.popen('stty size', 'r').read().split()
# print(lol)
def main():
    size = Size()
    rows, columns = size.getSize()
    print({},{}).format(size.getSize())
main()