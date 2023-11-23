import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class PhotoAlbumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Album App")

        self.photos = []
        self.current_photo_index = tk.IntVar()
        self.current_photo_index.set(0)

        self.create_widgets()

    def create_widgets(self):
        # Frame untuk menampilkan foto
        self.photo_frame = tk.Frame(self.root)
        self.photo_frame.pack(pady=10)

        self.photo_label = tk.Label(self.photo_frame)
        self.photo_label.pack()

        # Tombol untuk memilih foto
        self.upload_button = tk.Button(self.root, text="Unggah Foto", command=self.upload_photo)
        self.upload_button.pack(pady=10)

        # Tombol untuk melihat foto sebelumnya
        self.prev_button = tk.Button(self.root, text="Sebelumnya", command=self.show_prev_photo)
        self.prev_button.pack(side=tk.LEFT)

        # Tombol untuk melihat foto berikutnya
        self.next_button = tk.Button(self.root, text="Berikutnya", command=self.show_next_photo)
        self.next_button.pack(side=tk.RIGHT)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Pilih FOTO", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Salin foto ke direktori penyimpanan (ganti 'path_to_save' sesuai keinginan Anda)
            path_to_save = "path/to/save/directory"
            if not os.path.exists(path_to_save):
                os.makedirs(path_to_save)

            file_name = os.path.basename(file_path)
            save_path = os.path.join(path_to_save, file_name)

            # Salin file ke direktori penyimpanan
            if not os.path.exists(save_path):
                with open(file_path, 'rb') as source, open(save_path, 'wb') as target:
                    target.write(source.read())

            # Tambahkan foto ke daftar
            photo = Image.open(file_path)
            photo = ImageTk.PhotoImage(photo)
            self.photos.append(photo)

            if len(self.photos) == 1:
                self.show_photo()

    def show_photo(self):
        current_photo = self.photos[self.current_photo_index.get()]
        self.photo_label.config(image=current_photo)
        self.photo_label.photo = current_photo

    def show_prev_photo(self):
        if self.current_photo_index.get() > 0:
            self.current_photo_index.set(self.current_photo_index.get() - 1)
            self.show_photo()

    def show_next_photo(self):
        if self.current_photo_index.get() < len(self.photos) - 1:
            self.current_photo_index.set(self.current_photo_index.get() + 1)
            self.show_photo()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoAlbumApp(root)
    root.mainloop()
