import argparse
import os
import sys
from datetime import date

# done.txt exp

date_now = str(date.today())
print("X", date_now, "iam deleted todo")

f = open("done.txt", "a")
inp = str("X " + date_now + " iam deleted todo" + "\n")
f.write(inp)
f.close
print(type(inp))

