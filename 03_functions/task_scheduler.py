def add_task(task_name: str, task_list = None):
    if task_list is None:
        task_list = []
    task_list.append(task_name)
    return task_list
        
a = "buy stuff"
b = "throw away stuff"

print(add_task(a))
print(add_task(b))