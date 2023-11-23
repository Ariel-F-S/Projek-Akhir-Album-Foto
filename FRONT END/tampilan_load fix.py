from tkinter import Tk, Label, PhotoImage, Frame

class aplikasidekstop:
    def __init__(self,root):
        self.root = root
        root.title("My Memories")
        root.geometry("1920x1080")

        self.frame_utama = Frame(root, bg="#f0f0f0", padx=20, pady=20)
        self.frame_utama.pack(expand= True, fill="both")

        self.logo = PhotoImage(file="LOGO_ALBUM.png")

        self.logo_label = Label(self.frame_utama, image=self.logo)
        self.logo_label.pack(pady=250)

        self.welcome = Label(self.frame_utama, text ="Welcome", font=("Tahoma", 25))
        self.welcome.pack(padx= 20, pady= 20)

if __name__ == "__main__":
    root = Tk()
    app = aplikasidekstop(root)
    root.mainloop()
    