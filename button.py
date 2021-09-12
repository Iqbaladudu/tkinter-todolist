import tkinter as tk

main = tk.Tk()
"""
Write bellow
"""
main.title('Counting Seconds')
button = tk.Button(main, text="stop", width=25, command=main.destroy)
button.pack()

main.mainloop()