def add_task(tasks):
    while True:
        description = input("Enter the task description: ").strip()
        if not description:
            print("Task description cannot be empty. Please try again.")
        else:
            break
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print('Task added successfully!')

def your_name(name):
    print(f"Hello `{name}`, welcome to the todo app!")
    
def view_tasks(tasks):
    if not tasks:
        print('No tasks available.')
    task_list = []
    for i, task in enumerate(tasks, start=1):
        status = '✓' if task['completed'] else '✗'
        task_list.append(f"{i}. {task['description']} [{status}]")
    return "\n".join(task_list)

def mark_task_complete(tasks):
    if not tasks:
        print('No tasks to complete.')
        return
    view_tasks(tasks)
    try:
        task_num = int(input('Enter the tasks number to mark as complete: ')) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            print('Task marked as complete!')
        else:
            print('Invalid task number.')
    except ValueError:
        print('Please enter a valid number.')


def remove_task(tasks):
    if not tasks:
        print('No tasks to remove.')
        return
    view_tasks(tasks)
    try:
        task_num = int(input('Enter the task number to remove: ')) - 1
        if 0 <= task_num <= len(tasks):
            removed = tasks.pop(task_num)
            print(f"Task `{removed['description']}` removed successfully!")
        else:
            print('Please enter a valid number.')
    except ValueError:
        print('Please enter a valid number.')

def count_completed_tasks(tasks):
    return sum(1 for task in tasks if task['completed'])

def main():
    name = input('Enter your name: ')
    your_name(name)
    tasks = []
    while True:
        print('\nTo-Do List App')
        print('1. Add a Task')
        print('2. View Tasks')
        print('3. Mark Task as Complete')
        print('4. Remove a Task')
        print('5. Exit')
        print('6. Number of Completed Tasks')

        choice = input('Choose an option: ')

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            print(view_tasks(tasks))
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print('Goodbye!')
            break
        elif choice == '6':  
            completed_count = count_completed_tasks(tasks)
            print(f"Number of completed tasks: {completed_count}")
        else:
            print('Invalid choice. Please try again')



if __name__ == '__main__':
    main()
