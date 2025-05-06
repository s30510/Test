import tkinter as tk

# Funkcja obsługująca kliknięcie przycisku
def on_button_click():
    input_text = entry.get()  # Pobiera tekst z pola tekstowego
    label.config(text=f'Wprowadziłeś: {input_text}')  # Zmienia tekst etykiety

# Funkcja obsługująca zmiany w polu tekstowym
def on_text_change(*args):
    current_text = entry.get()
    label.config(text=f'Tekst: {current_text}')

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Przykładowa aplikacja GUI")
root.geometry("400x300")

# Etykieta wyświetlająca tekst
label = tk.Label(root, text="Wprowadź coś:", font=("Arial", 14))
label.pack(pady=20)

# Pole tekstowe, w którym użytkownik może wprowadzać tekst
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Przycisk, który wywoła funkcję on_button_click
button = tk.Button(root, text="Pokaż tekst", font=("Arial", 14), command=on_button_click)
button.pack(pady=10)

# Ustawiamy listener na zmiany w polu tekstowym (on_text_change)
entry.bind("<KeyRelease>", on_text_change)

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
