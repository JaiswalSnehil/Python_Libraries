import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

label = tk.Button(root, text='Click Me')
label.pack()

root.mainloop()