import tkinter
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
root=tkinter.Tk()
canvas=tkinter.Canvas(root, width=600, height=800)

canvas.grid(columnspan=3)
br_text=tkinter.StringVar()
br_button=tkinter.Button(root,text="select")


root.mainloop()