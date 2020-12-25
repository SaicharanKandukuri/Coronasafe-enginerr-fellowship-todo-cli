import sys as s
import os.path
from os import path
from datetime import date


help_string = """\
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics`;
"""
def add():
    def file_todo_txt():
        if path.exists("todo.txt"):
            return 1
        else:
            return 0
    
    if file_todo_txt():
        pass
    else:
        open("todo.txt", "x")

    if len(s.argv) == 3:
        f = open("todo.txt", "a")
        inp = str(s.argv[2]+"\n")
        f.write(inp)
        f.close
        print("Added todo: " + "\""+str(s.argv[2])+"\"")
    elif len(s.argv) == 2:
        print("Error: Missing todo string. Nothing added!")


def help():
    print(help_string)
def listtodo():
    if path.exists("todo.txt"):
        with open('todo.txt', 'r') as f:
            for i, line in reversed(list(enumerate(f, start=1))):
                print('[{}] {}'.format(i, line.strip()))
    else:
        print("There are no pending todos!")


def deltodo():
    if len(s.argv) == 3:
        tododel = open("todo.txt", "r")
        tododel_lines = tododel.readlines()
        tododel.close()
        
        reversed_todo = tododel_lines[::-1]
        input_numbe=str(s.argv[2])
        del_index=int(input_numbe)


        delnumtodo = del_index - 1

        def process():

            del tododel_lines[delnumtodo]


            new_todo_file = open("todo.txt", "w+")

            for line in tododel_lines:
                new_todo_file.write(line)


            print("Deleted todo #"+input_numbe)

        if del_index == 0:
            print("Error: todo #"+input_numbe+" does not exist. Nothing deleted.")
        elif del_index == 4:
            print("Error: todo #"+input_numbe+" does not exist. Nothing deleted.")
        elif del_index == 5:
            print("Error: todo #"+input_numbe+" does not exist. Nothing deleted.")
        else:
            process()

    elif len(s.argv) == 2:
        print("Error: Missing NUMBER for deleting todo.")
def donetodo():
    def file_done_txt():
        if path.exists("done.txt"):
            return 1
        else:
            return 0

    if  file_done_txt():
        pass
    else:
        open("done.txt", "x")
    
    def operate():
        global lines_in_todo
        todo_file = open("todo.txt", "r")
        linesg = todo_file.readlines()
        lines = linesg[::-1]
        lines_in_todo = int(len(lines))
    
    if len(s.argv) == 3:
       
       operate()

       no_line = str(s.argv[2])
       noline=int(no_line)
       if len(s.argv) == 3:
           todo_files_ = open("todo.txt", "r")
           todo_linesr = todo_files_.readlines()
           todo_files_.close()
           
           todo_lines = todo_linesr[::1]

           todo_line_number = noline - 1
           cache_todo_line = todo_lines[todo_line_number]

           done_format = ("x" +" "+ str(date.today()) +" "+ cache_todo_line)

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
           if noline == 0:
               print("Error: todo #0 does not exist.")
           else:
               print("Marked todo"+ " #"+str(noline)+" as done.")

    else:
        if len(s.argv) == 2:
            print("Error: Missing NUMBER for marking todo as done.")




def reporttodo():
    from datetime import date
    todo_filer = open("todo.txt", "r")
    todo_listener = todo_filer.readlines()
    notodos = str(len(todo_listener))

    done_filer = open("done.txt", "r")
    done_listener = done_filer.readlines()
    donetodos = str(len(done_listener))

    format_report = (str(date.today())+" Pending : "+notodos+" Completed : "+donetodos)

    print(format_report)

# 3
if len(s.argv) > 1:
    if str(s.argv[1]) == "add":
        add()
    elif str(s.argv[1]) == "help":
        help()
    elif str(s.argv[1]) == "ls":
        listtodo()
    elif str(s.argv[1]) == "del":
        deltodo()
    elif str(s.argv[1]) == "done":
        donetodo()
    elif str(s.argv[1]) == "report":
        reporttodo()
    else :
        print("Error unknown attribute")
else :
    print("No attribute specified")
    help()
