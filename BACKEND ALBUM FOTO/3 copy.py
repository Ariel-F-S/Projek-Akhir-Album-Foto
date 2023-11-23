import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class AlbumFoto:
    def __init__(self, root):
        self.root = root
        self.root.title("Album Foto")

        self.image_list = []
        self.current_index = 0

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        self.btn_prev = tk.Button(root, text="Previous", command=self.prev_image)
        self.btn_prev.pack(side=tk.LEFT)

        self.btn_next = tk.Button(root, text="Next", command=self.next_image)
        self.btn_next.pack(side=tk.RIGHT)

        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack()

        self.btn_save = tk.Button(root, text="Save Image", command=self.save_image)
        self.btn_save.pack()

        self.btn_delete = tk.Button(root, text="Delete Image", command=self.delete_image)
        self.btn_delete.pack()

        self.btn_favorite = tk.Button(root, text="Favorite", command=self.favorite_image)
        self.btn_favorite.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((600, 400))
            self.image_list.append({
                "path": file_path,
                "image": ImageTk.PhotoImage(img),
                "favorite": False
            })

            self.current_index = len(self.image_list) - 1
            self.show_image()

    def show_image(self):
        if self.image_list:
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_list[self.current_index]["image"])

    def next_image(self):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.show_image()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()

    def save_image(self):
        if self.image_list:
            img = self.image_list[self.current_index]["image"]
            img.save("saved_image.png")  # Menyimpan gambar ke dalam file baru

    def delete_image(self):
        if self.image_list:
            del self.image_list[self.current_index]
            if self.current_index >= len(self.image_list):
                self.current_index = max(0, len(self.image_list) - 1)
            self.show_image()

    def favorite_image(self):
        if self.image_list:
            self.image_list[self.current_index]["favorite"] = True
            messagebox.showinfo("Favorite", "Image marked as favorite!")

def main():
    root = tk.Tk()
    app = AlbumFoto(root)
    root.mainloop()

if __name__ == "__main__":
    main()
