import tkinter as tk
from tkinter import messagebox
import os

#criar janela principal
root = tk.Tk()
root.title("Lista de Tarefas")
root.geometry("300x400")

#entrada de texto para nova tarefa
taks_entry = tk.Entry(root, width=20)
taks_entry.pack(pady=10)

#listbox para mostrar tarefas
taks_listbox = tk.Listbox(root, width = 30, height = 10)
taks_listbox.pack(pady=10)

#carrega tareas de um arquivo
def load_tasks():
  if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
      tasks = file.readlines()
      for task in tasks:
        taks_listbox.insert(tk.END, task.strip())




#salvar tarefas em um arquivo
def save_tasks():
  with open("tasks.txt", "w") as file:
    taks = taks_listbox.get(0, tk.END)
    for task in taks:
      file.write(task + "\n")

#adicionar tarefas
def add_task():
    task = taks_entry.get()
    if task != "":
      taks_listbox.insert(tk.END, task)  # Correct indentation
      taks_entry.delete(0, tk.END)
      save_tasks()
    else:
      messagebox.showwarning("Aviso", "Por favor, insira uma tarefa")

#adicionar botão para adicionar tarefas / add task button
add_button = tk.Button(root, text="Adicionar Tarefa", command=add_task)
add_button.pack(pady=5)

#remover tarefa / remove taks
def remove_task():
  try:
    selected_task_index = taks_listbox.curselection()[0]
    taks_listbox.delete(selected_task_index)
    save_tasks()
  except IndexError:
    messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover")

#botão remover tarefa / remove task 
remove_button = tk.Button(root, text="Remover Tarefa", command=remove_task)
remove_button.pack(pady=5)

#carregar tarefas ao inciciar o programa / load tasks when program starts
load_tasks()
root.mainloop() 

