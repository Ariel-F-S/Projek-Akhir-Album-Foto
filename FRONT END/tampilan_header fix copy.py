import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class FullScreenApp:
    def __init__(self, master, **kwargs):
        self.master = master
        master.attributes('-fullscreen', True)  # Menjadikan jendela layar penuh

        # Menambahkan tombol untuk memilih gambar
        self.choose_image_button = tk.Button(master, text='Choose Image', command=self.choose_image)
        self.choose_image_button.pack()

        # Menampilkan gambar terpilih
        self.image_label = tk.Label(master)
        self.image_label.pack()

        master.bind('<F11>', self.toggle_fullscreen)
        master.bind('<Escape>', self.end_fullscreen)

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp')])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        # Menampilkan gambar di label
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def toggle_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', not self.master.attributes('-fullscreen'))

    def end_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', False)

if __name__ == '__main__':
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
