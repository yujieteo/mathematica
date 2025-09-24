#!/usr/bin/env python3
import sys

def bitgen(s):
    for c in s:
        for i in range(8):
            yield int((c & (0x80>>i)) != 0);

def bytegen(s):
    for c in s:
        yield c;

def run(fn = "comp.txt", compress = True):
   comp = open("comp.txt", "rb").read();
   bg = bitgen(comp);
   for i in range(10):
       print(i, next(bg));
   return;

if __name__ == "__main__":
    if sys.argv[1] == "c":
        run(sys.argv[2]);
    if sys.argv[1] == "x":
        run(sys.argv[2], False);

# ./ctw.py c comp.txt