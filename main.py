from tkinter import *
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")


def add_task():
    task = entry_task.get()
    date = entry_date.get()
    place = entry_place.get()

    if task != "" and date != "" and place != "":
        listbox_tasks.insert(tkinter.END, task, date, place)
        entry_task.delete(0, tkinter.END)
        entry_date.delete(0, tkinter.END)
        entry_place.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="can not find task.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


#Gui Work
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

add_taks_label = Label(root, text="Tasks")
add_taks_label.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

add_date_label = Label(root, text="Date")
add_date_label.pack()

entry_date = tkinter.Entry(root, width=50)
entry_date.pack()

add_place_label = Label(root, text="Place")
add_place_label.pack()

entry_place = tkinter.Entry(root, width=50)
entry_place.pack()

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load Task", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save Task", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()