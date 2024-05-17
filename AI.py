# user_prompt = "vazifalarni yozing:"
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
#
# todos = [todo1, todo2]
# print(todos)
#
#
# print(type(user_prompt))
# text = input("enter a title:")
#
# length = len(text)
#
# print(length)
# user_prompt = "Enter a to do:"
# #
# # while 2 > 1:
# #     todo = input(user_prompt)
# #     print(todo)
# #     print("Next...")
#
# user_prompt = "Enter a to do:"

# while True:
#     todo = input(user_prompt)
#     print(todo)
#     print("Next...")
#
# d = "Enter a todo:"
#
# todos = []
# while True:
#     todo = input(d)
#     todos.append(todo)
#     print(todos)
#
#


# todos = []
#
# while True:
#     choice = input("Type add, show and exit:")
#
#     match choice:
#         case "add":
#             todo = input("Enter a todo:")
#             todos.append(todo)
#         case "show":
#             for item in todos:
#                 print(item)
#         case "exit":
#             break
# print("hayr")

# todos = []
#
# while True:
#     user = input("Type add, show and exit:")
#     user = user.strip()
#
#     match user:
#         case "add":
#             todo = input("enter a todo:")
#             todos.append(todo)
#         case "show":
#             for item in todos:
#                 print(item)
#         case "exit":
#             break
# print("bye!")
# meal = ["salad", "sho'rva", "osh"]
#
# for melas in meal:
#     print(meal.capitalize())
#
# print("bye")

# todos = []
#
# while True:
#     user = input("Type add, show, edit and exit:")
#     user = user.strip()
#
#     match user:
#         case "add":
#             todo = input("enter a todo:")
#             todos.append(todo)
#         case "show":
#             for item in todos:
#                 print(item)
#         case "edit":
#             number = int(input("number of the todo to edit:"))
#             number = number - 1
#             existing_todo = todos[number]
#             print(existing_todo)
#
#         case "exit":
#             break
# print("bye!")



#todos = []

#while True:
 #    user_action = input("Type add, show, edit, complete or exit:")
  #   user_action = user_action.strip()

   #  match user_action:

    #     case "add":
     #        todo = input("Enter a todo:\n")

      #       file = open("todos.txt", "r")
       #      todos = file.readlines()
        #     file.close()

         #    todos.append(todo)


          #   # file = open("todos.txt", "w")
             # file.writelines(todos)

         #case "show":
          #   file=open('todos.txt', 'r')
           #  file.writelines(todos)
            # file.close()

             #for index, item in enumerate(todos):
              #   print(index+1, "-", item)

         #case "edit":
          #   number = int(input("Number of the todo to edit:"))
           #  number = number - 1
             #new_todo = input("Enter a new todo:\n")
            # todos[number]= new_todo

        # case "complete":
         #     number = int(input("Number of the todo to complete: "))
          #    todos.pop(number-1)


       #  case "exit":
        #     print("Good bye!!!")
         #    file = open("todos.txt", "w")
          #   file.writelines(todos)
           #  break

#from functions import get_todos, write_todos
import functions
import time

today=time.strftime("%b %d, %Y  %H:%M:%S")
print(f"It is {today}")

# text = """
# Principles of  productivity:
# Managing your inflow
# Systemizing everthing you want that repeats.
# """
#
# # text = "\
# # Principles of productivity: \
# # Managing your inflow\n\
# # Systemizing everthing you want that repeats.\
# # "



while True:
    user_action=input("Type add,show,edit,complete or exit:\n>>>")
    user_action=user_action.strip()


    if user_action.startswith("add"):
        todo=user_action[4:]

        # file=open("todos.txt",'r')
        # todos=file.readlines()
        # file.close()
        # with context manager
        todos= functions.get_todos()
        import time

        today = time.strftime("%b %d, %Y  %H:%M:%S")

        todos.append(todo.capitalize() + "       "  + today  + '\n' )

        # file=open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        functions.write_todos(todos)
    elif user_action.startswith("show"):

        todos= functions.get_todos()

        new_todos=[item.strip("\n") for item in todos]

        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)

            number=number-1

            todos= functions.get_todos()
            import time

            today = time.strftime("%b %d, %Y  %H:%M:%S")

            new_todo=input("Enter a new todo: ")
            todos[number]=new_todo.capitalize()+"  to do was edited in "+ today +"\n"

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue


    elif user_action.startswith("complete"):
            number=int(user_action[9:])

            todos= functions.get_todos()
            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message=f"Todo {todo_to_remove} was removed from the list."
            print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!!!")

print('Bye!')


