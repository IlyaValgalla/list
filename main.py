import tkinter as tk
from tkinter import simpledialog

# Создаем главное окно
root = tk.Tk()
root.title("To-Do List")

# Создаем пустой список для хранения дел
todo_list = []

# Функция для добавления дела в список
def add_todo():
    todo = simpledialog.askstring("Добавить дело", "Введите новое дело:")
    if todo:
        todo_list.append({"task": todo, "completed": False})
        update_listbox()

# Функция для удаления дела из списка
def remove_todo():
    selected_index = listbox.curselection()
    if selected_index:
        todo_list.pop(selected_index[0])
        update_listbox()

# Функция для обновления списка дел в окне
def update_listbox():
    listbox.delete(0, tk.END)
    for index, todo in enumerate(todo_list, start=1):
        status = "✓" if todo["completed"] else " "
        listbox.insert(tk.END, f"{index}. [{status}] {todo['task']}")

# Функция для отметки дела как выполненного
def toggle_completed():
    selected_index = listbox.curselection()
    if selected_index:
        todo = todo_list[selected_index[0]]
        todo["completed"] = not todo["completed"]
        update_listbox()

# Создаем список (Listbox) для отображения дел
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Создаем кнопки для добавления, удаления и отметки выполненного дела
add_button = tk.Button(root, text="Добавить дело", command=add_todo)
add_button.pack()
remove_button = tk.Button(root, text="Удалить дело", command=remove_todo)
remove_button.pack()
toggle_button = tk.Button(root, text="Отметить выполненное", command=toggle_completed)
toggle_button.pack()

# Запускаем основной цикл программы
root.mainloop()

