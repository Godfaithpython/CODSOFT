# To-Do List application in Python using a graphical user interface (GUI) with the Tkinter library:

import tkinter as tk
from tkinter import messagebox

# Function to create a new task


def create_task():
    task_name = task_name_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()

    if task_name and due_date and priority:
        task = {
            "name": task_name,
            "due_date": due_date,
            "priority": priority
        }

        task_list.insert(tk.END, task)
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Function to clear input entries


def clear_entries():
    task_name_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

# Function to delete a task


def delete_task():
    selected_indices = task_list.curselection()

    if selected_indices:
        confirm = messagebox.askyesno(
            "Confirm", "Are you sure you want to delete the selected task?")

        if confirm:
            for index in reversed(selected_indices):
                task_list.delete(index)
    else:
        messagebox.showinfo("Information", "Please select a task to delete.")

# Function to initialize the GUI


def initialize_gui():
    global task_name_entry, due_date_entry, priority_entry, task_list

    root = tk.Tk()
    root.title("To-Do List")

    # Task Entry Frame
    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    tk.Label(entry_frame, text="Task Name:").grid(row=0, column=0, sticky="e")
    task_name_entry = tk.Entry(entry_frame)
    task_name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(entry_frame, text="Due Date:").grid(row=1, column=0, sticky="e")
    due_date_entry = tk.Entry(entry_frame)
    due_date_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(entry_frame, text="Priority:").grid(row=2, column=0, sticky="e")
    priority_entry = tk.Entry(entry_frame)
    priority_entry.grid(row=2, column=1, padx=10, pady=5)

    add_button = tk.Button(entry_frame, text="Add Task", command=create_task)
    add_button.grid(row=3, columnspan=2, pady=10)

    # Task List Frame
    list_frame = tk.Frame(root)
    list_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_list = tk.Listbox(list_frame, width=50, yscrollcommand=scrollbar.set)
    task_list.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar.config(command=task_list.yview)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack(pady=10)

    root.mainloop()


# Run the GUI application
if __name__ == "__main__":
    initialize_gui()
