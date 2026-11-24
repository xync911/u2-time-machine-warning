"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a single warning label for a time machine, at most 120 characters.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
