import sys as s

tododel = open("todo.txt", "r")
tododel_lines = tododel.readlines()
tododel.close()

reversed_todo = tododel_lines[::-1]
input_numbe=str(s.argv[2])
del_index=int(input_numbe)
delnumtodo = del_index - 1

del reversed_todo[delnumtodo]


new_todo_file = open("todo.txt", "w+")

for line in tododel_lines:
    new_todo_file.write(line)


print("Deleted todo #"+input_numbe)