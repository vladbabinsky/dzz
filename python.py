import os
file_name = 'tasks.txt'

def add_task(task):
    with open(file_name, 'a') as file:
        file.write(task + '\n')
    print(f"Задача '{task}' додана.")

def show_tasks():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Список задач:")
                for task in tasks:
                    print(f"- {task.strip()}")
            else:
                print("Список задач пустий.")
    else:
        print("Файл із задачами відсутній. Список задач пустий.")

def clear_tasks():
    with open(file_name, 'w') as file:
        pass
    print("Усі задачі видалено.")

while True:
    print("\nМеню:")
    print("1. Додати нову задачу")
    print("2. Показати всі задачі")
    print("3. Видалити всі задачі")
    print("4. Вихід")

    choice = input("Оберіть опцію: ")

    if choice == '1':
        task = input("Введіть нову задачу: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        clear_tasks()
    elif choice == '4':
        print("До побачення!")
        break
    else:
        print("Cпробуйте ще раз")
