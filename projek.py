import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk

PHOTO_DIR = "photos"
FAV_DIR = "favorit"

os.makedirs(PHOTO_DIR, exist_ok=True)
os.makedirs(FAV_DIR, exist_ok=True)

THUMB_SIZE = (130, 130)

class Gallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Gallery")
        self.root.geometry("1100x650")
        self.root.configure(bg="#121212")

        self.selected_path = None
        self.thumb_refs = []

        # ===== HEADER =====
        header = tk.Frame(root, bg="#1e1e1e", height=50)
        header.pack(fill=tk.X)

        tk.Button(header, text="➕ Import", command=self.import_photos).pack(side=tk.LEFT, padx=10)
        tk.Button(header, text="⭐ Favorit", command=self.add_favorite).pack(side=tk.LEFT)
        tk.Button(header, text="🗑 Hapus", command=self.delete_photo).pack(side=tk.LEFT, padx=5)
        tk.Button(header, text="✏ Rename", command=self.rename_photo).pack(side=tk.LEFT, padx=5)
        tk.Button(header, text="▶ Slideshow", command=self.slideshow).pack(side=tk.LEFT, padx=5)

        # ===== MAIN =====
        main = tk.Frame(root, bg="#121212")
        main.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(main, bg="#121212", highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(main, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.gallery_frame = tk.Frame(self.canvas, bg="#121212")
        self.canvas.create_window((0, 0), window=self.gallery_frame, anchor="nw")

        self.gallery_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # ===== PREVIEW =====
        self.preview = tk.Label(root, bg="#121212")
        self.preview.pack(pady=5)

        self.load_gallery()

    # =========================
    def load_gallery(self):
        for w in self.gallery_frame.winfo_children():
            w.destroy()

        self.thumb_refs.clear()
        files = os.listdir(PHOTO_DIR)

        col = 0
        row = 0

        for file in files:
            path = os.path.join(PHOTO_DIR, file)

            try:
                img = Image.open(path)
                img.thumbnail(THUMB_SIZE)
                thumb = ImageTk.PhotoImage(img)

                frame = tk.Frame(self.gallery_frame, bg="#121212", bd=2)
                frame.grid(row=row, column=col, padx=10, pady=10)

                lbl = tk.Label(frame, image=thumb, bg="#121212", cursor="hand2")
                lbl.image = thumb
                lbl.pack()

                lbl.bind("<Button-1>", lambda e, p=path, f=frame: self.select_photo(p, f))

                self.thumb_refs.append(thumb)

                col += 1
                if col == 6:
                    col = 0
                    row += 1
            except:
                pass

    # =========================
    def select_photo(self, path, frame):
        self.selected_path = path

        for w in self.gallery_frame.winfo_children():
            w.config(bg="#121212")

        frame.config(bg="#2979ff")

        img = Image.open(path)
        img.thumbnail((400, 400))
        self.preview_img = ImageTk.PhotoImage(img)
        self.preview.config(image=self.preview_img)

    # =========================
    def import_photos(self):
        files = filedialog.askopenfilenames(
            filetypes=[("Images", "*.jpg *.png *.jpeg")]
        )
        for f in files:
            shutil.copy(f, PHOTO_DIR)
        self.load_gallery()

    # =========================
    def delete_photo(self):
        if self.selected_path:
            os.remove(self.selected_path)
            self.selected_path = None
            self.preview.config(image="")
            self.load_gallery()

    # =========================
    def add_favorite(self):
        if self.selected_path:
            shutil.copy(self.selected_path, FAV_DIR)
            messagebox.showinfo("Favorit", "Ditambahkan ke favorit")

    # =========================
    def rename_photo(self):
        if self.selected_path:
            new = simpledialog.askstring("Rename", "Nama baru:")
            if new:
                new_path = os.path.join(PHOTO_DIR, new)
                os.rename(self.selected_path, new_path)
                self.load_gallery()

    # =========================
    def slideshow(self):
        if not self.selected_path:
            return

        files = os.listdir(PHOTO_DIR)
        paths = [os.path.join(PHOTO_DIR, f) for f in files]

        win = tk.Toplevel(self.root)
        win.attributes("-fullscreen", True)
        lbl = tk.Label(win, bg="black")
        lbl.pack(expand=True)

        def show(i=0):
            img = Image.open(paths[i])
            img.thumbnail((900, 700))
            photo = ImageTk.PhotoImage(img)
            lbl.config(image=photo)
            lbl.image = photo
            win.after(2000, lambda: show((i + 1) % len(paths)))

        show()
        win.bind("<Escape>", lambda e: win.destroy())

# =============================
root = tk.Tk()
Gallery(root)
root.mainloop()