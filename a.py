tasks = [
    {'name': 'buy milk', 'isComplete': False},
    {'name': 'feed Max', 'isComplete': False}
]

def complete_todo(todo):
    for i in range(len(tasks)):
        if todo["name"] == tasks[i]["name"]:
            tasks[i]["isComplete"]=True #
    print(tasks)
            
complete_todo('buy milk')

