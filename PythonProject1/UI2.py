import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watchlist")
        self.geometry("400x400")

        # Tworzymy obie sceny jako ramki
        self.scene1 = Scene1(self, "To jest opis sceny 1: Możesz dodać filmy, oceny, komentarze itp.")
        self.scene2 = Scene2(self, "To jest opis sceny 2: Tutaj możesz filtrować filmy.")
        self.scene3 = Scene3(self, "To jest opis sceny 3: Podsumowanie, statystyki kolekcji filmów.")

        # Tworzymy pasek na dole z przyciskami
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill="x")

        # Tworzymy przyciski
        button1 = tk.Button(self.button_frame, text="Scena 1", command=self.show_scene1)
        button1.pack(side=tk.LEFT, fill="x", expand=True)

        button2 = tk.Button(self.button_frame, text="Scena 2", command=self.show_scene2)
        button2.pack(side=tk.LEFT, fill="x", expand=True)

        button3 = tk.Button(self.button_frame, text="Scena 3", command=self.show_scene3)
        button3.pack(side=tk.LEFT, fill="x", expand=True)

        # Na początku pokazujemy scenę 1
        self.show_scene1()

    def show_scene1(self):
        """Pokazuje scenę 1"""
        self.scene2.pack_forget()
        self.scene3.pack_forget()
        self.scene1.pack(fill="both", expand=True)

    def show_scene2(self):
        """Pokazuje scenę 2"""
        self.scene1.pack_forget()
        self.scene3.pack_forget()
        self.scene2.pack(fill="both", expand=True)

    def show_scene3(self):
        """Pokazuje scenę 3"""
        self.scene1.pack_forget()
        self.scene2.pack_forget()
        self.scene3.pack(fill="both", expand=True)


class Scene1(tk.Frame):
    def __init__(self, master, description):
        super().__init__(master)

        # Label informujący o scenie
       # label = tk.Label(self, text="To jest Scena 1", font=("Helvetica", 16))
      #  label.pack(pady=50)

        # Tworzymy pasek wyszukiwania
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=10, padx=10, fill="x")

        # Przykładowa lista elementów
        self.items = [
            "Apple", "Banana", "Orange", "Grape", "Pineapple",
            "Strawberry", "Blueberry", "Raspberry", "Mango", "Papaya"
        ]

        # Listbox do wyświetlania wyników
        self.listbox = tk.Listbox(self)
        self.listbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Na początku wypełniamy listbox wszystkimi elementami
        for item in self.items:
            self.listbox.insert(tk.END, item)

        # Nasłuchujemy na każdą zmianę tekstu w polu wyszukiwania
        self.search_entry.bind("<KeyRelease>", self.filter_list)

        # Wyświetlanie opisu
        description_label = tk.Label(self, text=description, font=("Helvetica", 12), wraplength=350)
        description_label.pack(pady=20)

    def filter_list(self, event=None):
        """Filtrowanie listy na podstawie tekstu z pola wyszukiwania"""
        search_text = self.search_entry.get().lower()

        # Wyczyść listbox
        self.listbox.delete(0, tk.END)

        # Dodaj do listboxa tylko elementy, które zawierają tekst z pola wyszukiwania
        for item in self.items:
            if search_text in item.lower():
                self.listbox.insert(tk.END, item)


class Scene2(tk.Frame):
    def __init__(self, master, description):
        super().__init__(master)

        label = tk.Label(self, text="To jest Scena 2", font=("Helvetica", 16))
        label.pack(pady=50)

        description_label = tk.Label(self, text=description, font=("Helvetica", 12), wraplength=350)
        description_label.pack(pady=10)


class Scene3(tk.Frame):
    def __init__(self, master, description):
        super().__init__(master)

        label = tk.Label(self, text="To jest Scena 3", font=("Helvetica", 16))
        label.pack(pady=50)

        description_label = tk.Label(self, text=description, font=("Helvetica", 12), wraplength=350)
        description_label.pack(pady=10)


# Uruchamiamy aplikację
if __name__ == "__main__":
    app = Application()
    app.mainloop()
