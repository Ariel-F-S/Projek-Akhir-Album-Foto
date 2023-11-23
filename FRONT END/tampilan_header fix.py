import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Memories")

        # Header
        self.header_frame = tk.Frame(self.root, bg="#f0f0f0", height=100)
        self.header_frame.grid(row=0, column=0, columnspan=4, sticky="ew")  

        # Configure row and column weights
        self.root.grid_rowconfigure(1, weight=1)
        for i in range(6):
            self.root.grid_columnconfigure(i, weight=1)

        # Logo
        image = ImageTk.PhotoImage(file="LOGO_ALBUM.png")
        original_image = Image.open("LOGO_ALBUM.png")
        resized_image = original_image.resize((75, 75))
        self.logo_image = ImageTk.PhotoImage(resized_image)
        self.logo_label = tk.Label(self.header_frame, image=self.logo_image, padx=10)
        self.logo_label.grid(row=0, column=0, padx=(10, 0), pady=5, sticky="w")
        self.logo_label.image = image

        # Judul "My Memories"
        self.title_label = tk.Label(self.header_frame, text="My Memories", fg="black", bg="#f0f0f0")
        self.title_label.grid(row=0, column=1, padx=(0, 10), pady=5, sticky="w")

        # Search Bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.header_frame, textvariable=self.search_var, bg="white", fg="black", insertbackground="white")
        self.search_entry.grid(row=0, column=4, padx=10, pady=20, sticky="e")

        # Button Search
        self.search_button = tk.Button(self.header_frame, text="Search", command=self.perform_search, bg="#f0f0f0", fg="black")
        self.search_button.grid(row=0, column=5, padx=10, pady=20, sticky="e")

        # isi
        self.frame = tk.Frame(self.root, bg="black", height=1030)
        self.frame.grid(row=1, column=0, columnspan=6, sticky="nsew")  

        # Kotak 1
        self.box_frame1 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame1.grid(row=0, column=10, padx=100, pady=200, sticky="nsew")  # Updated parameters

        # Kotak 2
        self.box_frame2 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame2.grid(row=0, column=20, padx=190, pady=200, sticky="nsew")  # Updated parameters

        # Kotak 3
        self.box_frame3 = tk.Frame(self.frame, bg="white", width=200, height=200)
        self.box_frame3.grid(row=0, column=25, padx=250, pady=200, sticky="nsew")  # Updated parameters

    def perform_search(self):
        search_query = self.search_var.get()
        print(f"Performing search for: {search_query}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
