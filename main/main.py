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



todos = []

while True:
     user_action = input("Type add, show, edit, complete or exit:")
     user_action = user_action.strip()

     match user_action:

         case "add":
             todo = input("Enter a todo:\n")

             file=open('todos.txt',"r")
             todos=file.readlines()
             file.close()

             new_todos=[]



             for item in todos:
                 new_item=item.strip('n')
                 new-todos.append(new_item)
             print(todos)

             for index,item in enumerate9=(new_todos):
                 row=f"{index+1}-{item}"
                 print(row)

             file=writelines(todos)
             file.close

             todos.append(todo)

             file = open("todos.txt", "w")
             file.writelines(todos)

         case "show":
             file = open('todos.txt', "r")
             todos = file.readlines()
             file.close()

             new_todos = [item.strip("\n") for item in todos]

             for item in todos:
                 new_item = item.strip('n')
                 new - todos.append(new_item)
             print(todos)

             for index, item in enumerate9=(new_todos):
                 row = f"{index + 1}-{item}"
                 print(row)



         case "edit":
             number = int(input("Number of the todo to edit:"))
             number = number - 1
             new_todo = input("Enter a new todo:\n")
             todos[number]= new_todo

         case "complete":
              number = int(input("Number of the todo to complete: "))
              todos.pop(number-1)


         case "exit":
             print("Good bye!!!")
             file = open("todos.txt", "w")
             file.writelines(todos)
             break



