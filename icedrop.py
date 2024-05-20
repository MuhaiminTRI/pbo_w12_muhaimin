import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi untuk Mendeskripsikan Gambar")

        # Membuat frame utama
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Membuat label
        self.label = ttk.Label(self.main_frame, text="Masukkan teks:")
        self.label.grid(row=0, column=0, pady=5)

        # Membuat entry
        self.entry = ttk.Entry(self.main_frame, width=40)
        self.entry.grid(row=0, column=1, pady=5, padx=5)

        # Membuat tombol tampilkan
        self.display_button = ttk.Button(self.main_frame, text="Tampilkan", command=self.display_text)
        self.display_button.grid(row=0, column=2, pady=5)

        # Membuat tombol edit
        self.edit_button = ttk.Button(self.main_frame, text="Edit", command=self.edit_text)
        self.edit_button.grid(row=0, column=3, pady=5)

        # Membuat Label untuk menampilkan teks
        self.text_label = tk.Label(self.main_frame, text="", background="white", anchor="nw", justify="left", width=50, height=10, relief="solid")
        self.text_label.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky=(tk.W, tk.E))

        # Membuat Listbox untuk menampilkan teks
        self.listbox = tk.Listbox(self.main_frame, height=10, width=50)
        self.listbox.grid(row=2, column=0, columnspan=4, pady=5, padx=5, sticky=(tk.W, tk.E))

        # Membuat canvas
        self.canvas = tk.Canvas(self.main_frame, width=200, height=200, background='lightblue')
        self.canvas.grid(row=3, column=0, columnspan=4, pady=10)

        # Tombol untuk memasukkan gambar
        self.image_button = ttk.Button(self.main_frame, text="Masukkan Gambar", command=self.load_image)
        self.image_button.grid(row=4, column=0, columnspan=4, pady=5)

        self.image = None
        self.image_id = None

    def display_text(self):
        # Mengambil teks dari entry dan menambahkannya di Listbox
        input_text = self.entry.get()
        if input_text.strip():  # Cek apakah teks tidak kosong atau hanya spasi
            self.listbox.insert(tk.END, input_text)
            self.entry.delete(0, tk.END)
            self.update_label()

    def edit_text(self):
        # Mengambil teks yang dipilih dari Listbox untuk diedit
        try:
            selected_index = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_index)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected_text)

            def save_edit():
                edited_text = self.entry.get()
                if edited_text.strip():  # Cek apakah teks tidak kosong atau hanya spasi
                    self.listbox.delete(selected_index)
                    self.listbox.insert(selected_index, edited_text)
                    self.entry.delete(0, tk.END)
                    self.update_label()
                    self.entry.config(state=tk.NORMAL)
                    self.save_button.destroy()
                    self.cancel_button.destroy()

            def cancel_edit():
                self.entry.delete(0, tk.END)
                self.entry.config(state=tk.NORMAL)
                self.save_button.destroy()
                self.cancel_button.destroy()

            self.save_button = ttk.Button(self.main_frame, text="Save", command=save_edit)
            self.save_button.grid(row=0, column=4, pady=5)

            self.cancel_button = ttk.Button(self.main_frame, text="Cancel", command=cancel_edit)
            self.cancel_button.grid(row=0, column=5, pady=5)

            self.entry.config(state=tk.NORMAL)

        except IndexError:
            pass

    def update_label(self):
        # Mengupdate teks di Label dengan teks dari Listbox
        all_text = "\n".join(self.listbox.get(0, tk.END))
        self.text_label.config(text=all_text)

    def load_image(self):
        # Memilih file gambar
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
        if file_path:
            # Membuka dan mengubah ukuran gambar
            image = Image.open(file_path)
            image.thumbnail((200, 200))  # Mengatur ukuran thumbnail
            self.image = ImageTk.PhotoImage(image)
            
            # Menghapus gambar sebelumnya jika ada
            if self.image_id:
                self.canvas.delete(self.image_id)

            # Menampilkan gambar pada canvas
            self.image_id = self.canvas.create_image(100, 100, image=self.image, anchor=tk.CENTER)

# Membuat instance dari Tkinter
root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
