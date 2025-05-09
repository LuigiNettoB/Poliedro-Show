import tkinter as tk
from tkinter import font

root = tk.Tk()
for f in font.families():
    print(f)
root.destroy()


