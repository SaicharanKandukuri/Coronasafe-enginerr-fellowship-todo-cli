from datetime import date
todo_filer = open("todo.txt", "r")
todo_listener = todo_filer.readlines()
notodos = str(len(todo_listener))

done_filer = open("done.txt", "r")
done_listener = done_filer.readlines()
donetodos = str(len(done_listener))

format_report = (str(date.today())+" Pending : "+notodos+" Completed : "+donetodos)

print(format_report)