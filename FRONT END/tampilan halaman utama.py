import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk

class DesktopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop App")
        self.root.geometry("1920x1080")

        # Kotak 1
        self.box_frame1 = tk.Frame(self.root, bg="white", width=200, height=200)
        self.box_frame1.grid(row=0, column=1, padx=50, pady=200)

        # Kotak 2
        self.box_frame2 = tk.Frame(self.root, bg="white", width=200, height=200)
        self.box_frame2.grid(row=0, column=2, padx=200, pady=200)

        # Kotak 3
        self.box_frame3 = tk.Frame(self.root, bg="white", width=200, height=200)
        self.box_frame3.grid(row=0, column=3, padx=40, pady=200)

        # Gambar 1
        self.image_frame1 = tk.Frame(self.root, bg="white")
        self.image_frame1.grid(row=1, column=0, padx=50, pady=10)

        # Gambar 2
        self.image_frame2 = tk.Frame(self.root, bg="white")
        self.image_frame2.grid(row=2, column=0, padx=70, pady=10)

        # Gambar 3
        self.image_frame3 = tk.Frame(self.root, bg="white")
        self.image_frame3.grid(row=3, column=0, padx=90, pady=10)

        # Tombol tambah gambar
        self.add_button = tk.Button(self.root, text="+", command=self.add_image, font=("Helvetica", 16), width=3, height=1, bg="black", fg="white")
        self.add_button.grid(row=4, column=3, padx=10, pady=10, sticky="se")

    def add_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            try:
                original_image = Image.open(file_path)
                resized_image = original_image.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized_image)

                # Menambahkan gambar ke frame gambar
                if not hasattr(self, 'image_label1'):
                    self.image_label1 = tk.Label(self.image_frame1, image=photo, bg="white")
                    self.image_label1.image = photo
                    self.image_label1.pack()
                elif not hasattr(self, 'image_label2'):
                    self.image_label2 = tk.Label(self.image_frame2, image=photo, bg="white")
                    self.image_label2.image = photo
                    self.image_label2.pack()
                elif not hasattr(self, 'image_label3'):
                    self.image_label3 = tk.Label(self.image_frame3, image=photo, bg="white")
                    self.image_label3.image = photo
                    self.image_label3.pack()

            except Exception as e:
                print(f"Error loading image: {e}")

        self.total_gambar = PhotoImage(file="ICON IMAGE.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopApp(root)
    root.mainloop()
