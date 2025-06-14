# def findNames(names=['aikol', 'geraim', 'max'], input='ai'):
#     # input is 'ai 
#     #output list of strings[]
#     found_name = []
#     for name in names:
#         input_length = len(input)
#         prefix = name[:input_length]
        
#         if prefix == input:
#             found_name.append(name)
#     return found_name

# print(findNames())
# Front end
# tasks = [
#         {   
#     'name': 'buy milk',
#     'isComplete': False,
#     },
#     {'name': 'feed Max',
#     'isComplete': False
#     }
# ]

# def complete_todo(todo):
#     for i in range(len(tasks)):
#         if todo.name == tasks[i].name:
#             tasks[i].isComplete=True #
#             print(tasks)
            
# print(complete_todo({'name': 'buy milk','isComplete': False}))