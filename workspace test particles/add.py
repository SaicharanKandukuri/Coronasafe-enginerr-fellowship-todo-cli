####################
import sys as s

import os.path
from os import path

####################

def file_todo_txt():
    if path.exists("todo.txt"):
        return 1
    else:
        return 0

if file_todo_txt() :
    pass
else:
    open("data.txt", "x")

if len(s.argv) == 3:
    f = open("todo.txt", "a")
    inp = str(s.argv[3])
    f.write(inp)
    f.close
elif len(s.argv) >= 4:
    print("Error : More than 1 attribure specified to add")
    help()
elif len(s.argv) == 2:
    print("Eroor No string specified")
    help()
