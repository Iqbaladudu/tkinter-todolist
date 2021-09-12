from tkinter import *
import tkinter as tk


class ToDoItem:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TodoListApp:

    def __init__(self, root):
        root.title("To Do List")
        #specific windows size
        # root.geometry("500x400")
        # root.maxsize(1000, 800)
        frame = Frame(root, width=200, height=100,relief='sunken', borderwidth=2)
        frame.grid(column=1, row=1, sticky=(N, E, S, W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)
        list_label = Label(frame, text="To Do List Items")
        list_label.grid(column=1, row=1, sticky=(S, W))
        self.to_do_item = [
            ToDoItem("Murajaah","Satu Juz"),
            ToDoItem("Baca Buku", "100 Halaman"),
            ToDoItem("Arabic","Satu Bab"),
        ]
        
        # list box
        # self.list_item_strings = ["Hei","Hi","Halo"]
        self.to_do_names = StringVar(value=list(map(lambda x: x.name, self.to_do_item)))
        item_list = Listbox(frame, listvariable=self.to_do_names)
        # listbox.pack(side=tk.BOTTOM, padx=10, pady=5)
        item_list.grid(column=1, row=2, sticky=(E, W))
        # specify hight
        item_list["height"] = 3
        # list binding
        item_list.bind("<<ListboxSelect>>", lambda s: self.select_item(item_list.curselection()))
        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable=self.selected_description)
        selected_description_label.grid(column=1, row=3, sticky=(E, W))
        self.label_text = StringVar()
        label = Label(frame, textvariable=self.label_text)
        # label.grid(column=1, row=1)
        # label.pack(side=tk.BOTTOM, padx=10, pady=10)
        # update label widget one by one
        # label["text"] = "New Label"
        # label["bg"] = "blue"
        # label["font"] = ("Courier", 40)
        
        # bulk add all
        label.configure(font=("Courier", 30))
        
        # text input
        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)
        # entry.place(x=100, y=50)
        # entry.grid(column=3, row=1)
        # entry.pack(side=tk.BOTTOM)
        
        # binding entry text to label
        # label['textvariable'] = entry_text
        
        # Button
        button = Button(frame, text="Button text", command=self.press_button)
        # button.place(x=0, y=0)
        # button.pack(side=tk.BOTTOM)
        # button.grid(column=1, row=2, sticky=(S, E))
        button.configure(width=10, height=1, font=("Courier", 30))

        
        
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
    def select_item(self, index):
        selected_item = self.to_do_item[index[0]]
        self.selected_description.set(selected_item.description)

root = Tk()
TodoListApp(root)
root.mainloop()