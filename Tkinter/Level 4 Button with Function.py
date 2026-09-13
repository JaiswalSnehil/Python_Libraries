import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

button = tk.Button(root, text='Click Me')
command = say_hello()
button.pack()

root.mainloop()