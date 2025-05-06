import tkinter as tk


def filter_list():
    # Pobierz tekst z Entry
    search_text = search_entry.get().lower()

    # Wyczyść listbox
    listbox.delete(0, tk.END)

    # Dodaj do listboxa tylko elementy, które zawierają tekst z pola wyszukiwania
    for item in items:
        if search_text in item.lower():
            listbox.insert(tk.END, item)


# Utworzenie głównego okna
root = tk.Tk()
root.title("Okno z wyszukiwarką")
root.geometry("300x400")

# Etykieta dla pola wyszukiwania
search_label = tk.Label(root, text="Wyszukaj:")
search_label.pack(pady=10)

# Pole wyszukiwania (Entry)
search_entry = tk.Entry(root)
search_entry.pack(pady=5, padx=10, fill="x")

# Przycisk do filtrowania listy
search_button = tk.Button(root, text="Szukaj", command=filter_list)
search_button.pack(pady=5)

# Lista elementów
items = [
    "Apple", "Banana", "Orange", "Grape", "Pineapple",
    "Strawberry", "Blueberry", "Raspberry", "Mango", "Papaya"
]

# Listbox do wyświetlania wyników
listbox = tk.Listbox(root)
listbox.pack(pady=10, padx=10, fill="both", expand=True)

# Wypełnij listbox początkowymi elementami
for item in items:
    listbox.insert(tk.END, item)

# Uruchamiamy główną pętlę
root.mainloop()
