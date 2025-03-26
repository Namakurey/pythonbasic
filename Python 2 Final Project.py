#GUI CRUD (create read update delete)
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, Entry
import random

root = tk.Tk()
root.title("GUI CRUD")
root.geometry('1000x500')
root.resizable(False, False) #x, y

# canvas = tk.Canvas(root, width=1000, height=500)
# canvas.pack()
# 
# def hex_to_rgb(hex_color):
#     """Convert a hexadecimal color to an RGB tuple."""
#     hex_color = hex_color.lstrip('#')
#     return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
#
# def create_gradient(canvas, width, height):
#     """Create a horizontal gradient on the canvas with random colors."""
#     # Generate two random colors
#     start_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Random hex color
#     end_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))    # Random hex color
#
#     # Convert hex colors to RGB tuples
#     r1, g1, b1 = hex_to_rgb(start_color)
#     r2, g2, b2 = hex_to_rgb(end_color)
#
#     # Create the gradient
#     for i in range(width):
#         # Interpolate the color at this column
#         r = int(r1 + (r2 - r1) * i / width)
#         g = int(g1 + (g2 - g1) * i / width)
#         b = int(b1 + (b2 - b1) * i / width)
#         color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
#
#         # Draw a vertical line with the current color
#         canvas.create_line(i, 0, i, height, fill=color)
#
# # Create the main window
# root = tk.Tk()
# root.geometry("1000x500")
# root.title("Random Gradient Background")
#
# # Create a Canvas to draw the gradient
# canvas = tk.Canvas(root, width=1000, height=500)
# canvas.pack()
#
# # Generate and display the random gradient
# create_gradient(canvas, 1000, 500)
#
#


#tampil
Tulisan_Tampil = Label(root, text="Tampil:", font=('Arial', 10))
Tulisan_Tampil.place(x = 500, y = 50)
Isian_Tampil = tk.Text(root, font=('Arial', 10), state='disabled', wrap=tk.WORD)
Isian_Tampil.place(x = 500, y = 75, width = 350, height = 150)

#nama file
Tulisan_Nama_File = Label(root, text="Nama file: ", font=('Arial', '10'))
Tulisan_Nama_File.place(x = 40, y = 20)

teks1 = tk.StringVar()
Isian_Nama_File = Entry(root, text=teks1, font=('Arial', '10'))
Isian_Nama_File.place(x = 110, y = 20)

#teks
Tulisan_Teks = Label(root, text="Teks:", font=('Arial', '10'))
Tulisan_Teks.place(x = 40, y = 50)

Isian_Teks = tk.Text(root, font=('Arial', '10'), wrap=WORD)
#tk.Text itu package.class() untuk multiline
#wrap=tk.WORD atau CHAR atau NONE itu supaya kalau sudah full linenya dia otomatis turun ke line bawahnya
Isian_Teks.place(x = 40, y = 75, width = 350, height = 150)

#delete file
Tulisan_file = Label(root, text="File:", font=('Arial', 10))
Tulisan_file.place(x = 40, y = 350)

teks4 = tk.StringVar()
Isian_DeleteFile = Entry(root, text=teks4, font=('Arial', 10))
Isian_DeleteFile.place(x = 40, y = 380)

#tombol create
def create():
    judul = Isian_Nama_File.get()
    text = Isian_Teks.get('1.0', tk.END)  # line 0, column 0
    with open(judul, 'w') as file:
        file.write(text)
    Isian_Tampil.configure(state='normal') #state= bisa normal(enabled to modify) atau disabled
    Isian_Tampil.delete('1.0', tk.END)
    Isian_Tampil.insert('1.0', text)
    Isian_Teks.delete('1.0', tk.END)
    Isian_Tampil.configure(state='disabled')
Tombol_Create = Button(root, text='Create', font=('Arial', 10), command=create)
Tombol_Create.place(x = 400, y = 90)

# tombol append
def nambah_text():
    judul = Isian_Nama_File.get().strip()
    tulisan = Isian_Teks.get('1.0', tk.END)
    Isian_Tampil.config(state='normal')
    Isian_Tampil.insert('end', tulisan)
    with open(judul, 'a') as file:
        file.write(tulisan)
    Isian_Teks.delete('1.0', tk.END)
    Isian_Tampil.config(state='disabled')
Tombol_Append = Button(root, text='Append', font=('Arial', 10), command=nambah_text)
Tombol_Append.place(x=400, y=150)

#tombol read
def membaca():
    judul = Isian_Nama_File.get().strip()
    try:
        with open(judul, 'r') as file:
            isifile = file.read()
        Isian_Tampil.config(state='normal')
        Isian_Tampil.delete('1.0', tk.END)
        Isian_Tampil.insert('1.0', isifile)
        Isian_Tampil.config(state='disabled')
    except FileNotFoundError:
        Isian_Tampil.config(state='normal')
        Isian_Tampil.delete('1.0', tk.END)
        Isian_Tampil.insert('1.0', f"File '{judul}' not found!")
        Isian_Tampil.config(state='disabled')

Tombol_Read = Button(root, text="Read", font=('Arial', 10), command=membaca)
Tombol_Read.place(x = 860, y = 90)

#search text
Tulisan_Search_Text = Label(root, text="Search Text: ", font=('Arial', 10))
Tulisan_Search_Text.place(x = 40, y = 270)

teks2 = tk.StringVar()
Isian_Search_Text = Entry(root, text=teks2, font=('Arial', 10))
Isian_Search_Text.place(x = 40, y = 300)

#Update text
Tulisan_Update_Text = Label(root, text="Update Text: ", font=('Arial', 10))
Tulisan_Update_Text.place(x = 200, y = 270)

teks3 = tk.StringVar()
Isian_Update_Text = Entry(root, text=teks3, font=('Arial', 10))
Isian_Update_Text.place(x = 200, y = 300)

#tombol update
def update():
    try:
        katasearch = Isian_Search_Text.get()
        kataupdate = Isian_Update_Text.get()
        judul = Isian_Nama_File.get().strip()
        with open(judul, 'r') as file:
            file_contents = file.read()
            if katasearch in file_contents:
                    perbaikan = file_contents.replace(katasearch, kataupdate)
                    Isian_Tampil.config(state='normal')
                    Isian_Tampil.delete('1.0', tk.END)
                    Isian_Tampil.insert('1.0', perbaikan)
                    with open(judul, 'w') as data:
                        data.write(perbaikan)
    except FileNotFoundError:
        Isian_Tampil.config(state='normal')
        Isian_Tampil.insert('1.0', "Please enter a valid file name!")
        Isian_Tampil.config(state='disabled')
Tombol_Update = Button(root, text="Update", font=('Arial', 10), command=update)
Tombol_Update.place(x = 350, y = 295)

#tombol delete
def deletefile():
    judul = Isian_DeleteFile.get().strip()
    try:
        os.remove(judul)
    except FileNotFoundError:
        Isian_Tampil.config(state='normal')
        Isian_Tampil.insert('1.0', "Please enter a valid file name!")
        Isian_Tampil.config(state='disabled')

Tombol_Delete = Button(root, text="Delete", font=('Arial', 10), command=deletefile)
Tombol_Delete.place(x = 190, y = 375)

#tambahan
Tombol_Done = Button(root, text='Done', font=('Arial', 18, 'bold'), command=root.destroy)
Tombol_Done.place(x = 700, y = 380)
mainloop()