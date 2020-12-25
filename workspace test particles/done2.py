import sys as s
import os.path
from os import close, path
from datetime import date

def file_done_txt():
    if path.exists("done.txt"):
        return 1
    else:
        return 0
    
if file_done_txt():
    pass
else:
    open("todo.txt", "x")
    # todo :

def operate():
    global lines_in_todo
    todo_file = open("todo.txt", "r")
    lines = todo_file.readlines()
    lines_in_todo = int(len(lines))

if len(s.argv) == 3:
    operate()

    noline = int(str(s.argv[2]))

    if noline <= lines_in_todo:
        todo_files_ = open("todo.txt", "r")
        todo_lines = todo_files_.readline()
        todo_files_.close()

        

        todo_line_number = noline - 1

        cache_todo_line = todo_lines[todo_line_number]

        done_format = ("x" + str(date.today()) + cache_todo_line)

        d = open("done.txt", "a")
        inp_done = done_format
        d.write(inp_done)
        d.close()
    
        line_to_delete = noline - 1

        del todo_lines[line_to_delete]

        new_todo_file = open("todo.txt", "w+")

        for line in todo_lines:
            new_todo_file.write(line)
        
        new_todo_file.close()
        print("Mareked todo: "+ "\#"+noline+" as done")
    elif noline > lines_in_todo:
        print("Error : line number "+"\""+noline+"\""+"dosen't exist try running ./todo ls to see line numbers")
        help()
    elif noline == 0:
        print("Error : No line indexed 0")
    

