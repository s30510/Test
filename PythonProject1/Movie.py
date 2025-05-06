import tk

class Movie:
    def __init__(self, title, director, year, genre, status, rating, description):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.status = status
        self.rating = rating
        self.description = description
        self.watch_date = None




my_movies = []



import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Informacja", "To jest komunikat!")

def get_input():
    text = entry.get()
    print("Wprowadzone dane:", text)

def on_checkbutton_click():
    if check_var.get() == 1:
        print("Checkbox jest zaznaczony.")
    else:
        print("Checkbox nie jest zaznaczony.")

def on_radiobutton_click(value):
    print(f"Wybrano opcję: {value}")

def update_label():
    label.config(text="Label zmieniony!")

def draw_on_canvas():
    canvas.create_oval(10, 10, 200, 200, fill="blue")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Program z widżetami Tkinter")
root.geometry("600x400")

# Label
label = tk.Label(root, text="To jest Label", font=("Helvetica", 14))
label.pack()

# Button
button = tk.Button(root, text="Pokaż komunikat", command=show_message)
button.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Button do wczytania tekstu z Entry
get_text_button = tk.Button(root, text="Pobierz tekst z Entry", command=get_input)
get_text_button.pack()

# Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Akceptuję warunki", variable=check_var, command=on_checkbutton_click)
checkbutton.pack()

# Radiobuttons
radiobutton1 = tk.Radiobutton(root, text="Opcja 1", value="1", command=lambda: on_radiobutton_click("Opcja 1"))
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(root, text="Opcja 2", value="2", command=lambda: on_radiobutton_click("Opcja 2"))
radiobutton2.pack()

# Listbox
listbox = tk.Listbox(root)
listbox.insert(tk.END, "Element 1")
listbox.insert(tk.END, "Element 2")
listbox.insert(tk.END, "Element 3")
listbox.pack()

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Canvas
canvas = tk.Canvas(root, width=300, height=300, bg="lightgray")
canvas.pack()

# Frame
frame = tk.Frame(root, borderwidth=2, relief="solid")
frame.pack(fill="both", expand=True)

# Scale
scale = tk.Scale(root, from_=0, to=100)
scale.pack()

# Spinbox
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# PanedWindow
panedwindow = tk.PanedWindow(root)
panedwindow.pack(fill="both", expand=True)

# Dodajemy widżety do PanedWindow
left_frame = tk.Frame(panedwindow, bg="lightblue", width=200, height=200)
left_frame.pack(fill="both", expand=True)
panedwindow.add(left_frame)

right_frame = tk.Frame(panedwindow, bg="lightgreen", width=200, height=200)
right_frame.pack(fill="both", expand=True)
panedwindow.add(right_frame)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Wyjście", command=root.quit)

# Button do rysowania na Canvasie
draw_button = tk.Button(root, text="Narysuj Okrąg", command=draw_on_canvas)
draw_button.pack()

# Button do zmiany tekstu w Label
change_label_button = tk.Button(root, text="Zmień tekst w Label", command=update_label)
change_label_button.pack()

# Uruchamiamy główną pętlę
root.mainloop()
