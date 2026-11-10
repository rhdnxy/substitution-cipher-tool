import random
import tkinter as tk
from tkinter import messagebox

class KriptoUnik:
    def __init__(self):
        self.karakter_asal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
        
        self.karakter_tujuan = (
            [chr(i) for i in range(0x0621, 0x064A)] + # Arab
            [chr(i) for i in range(0x0410, 0x044F)] + # Rusia
            [chr(i) for i in range(0x0E01, 0x0E3A)]   # Thai
        )
        
        random.seed(42) 
        tujuan_acak = list(self.karakter_tujuan)
        random.shuffle(tujuan_acak)
        
        self.map_enkripsi = dict(zip(self.karakter_asal, tujuan_acak))
        self.map_dekripsi = dict(zip(tujuan_acak, self.karakter_asal))

    def enkripsi(self, teks):
        try:
            return "".join(self.map_enkripsi.get(char, char) for char in teks)
        except Exception as e:
            return f"Error: {e}"

    def dekripsi(self, teks):
        try:
            return "".join(self.map_dekripsi.get(char, char) for char in teks)
        except Exception as e:
            return f"Error: {e}"

def run_gui():
    # Inisialisasi KriptoUnik
    kripto = KriptoUnik()

    # Membuat Jendela Utama
    root = tk.Tk()
    root.title("Substitution Cipher Tool")
    root.geometry("550x450") # Sedikit dilebarkan secara vertikal
    root.configure(padx=20, pady=20)
    root.resizable(False, False)

    # Label Judul
    lbl_title = tk.Label(root, text="SUBSTITUTION CIPHER TOOL", font=("Arial", 14, "bold"))
    lbl_title.pack(pady=(0, 15))

    # Fungsi Copy dan Paste
    def aksi_paste():
        try:
            # Mengambil teks dari clipboard bawaan sistem
            teks_clipboard = root.clipboard_get()
            txt_input.delete("1.0", tk.END) # Kosongkan input sebelumnya
            txt_input.insert(tk.END, teks_clipboard)
        except tk.TclError:
            messagebox.showwarning("Peringatan", "Clipboard kosong atau tidak berisi teks!")

    def aksi_copy():
        teks_hasil = txt_output.get("1.0", tk.END).strip("\n")
        if teks_hasil:
            root.clipboard_clear() # Bersihkan clipboard sistem
            root.clipboard_append(teks_hasil) # Masukkan teks hasil ke clipboard
            messagebox.showinfo("Berhasil", "Teks berhasil disalin ke clipboard!")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada teks yang bisa disalin!")

    # --- AREA INPUT ---
    frame_input_label = tk.Frame(root)
    frame_input_label.pack(fill="x")
    
    tk.Label(frame_input_label, text="Masukkan Teks:").pack(side="left")
    btn_paste = tk.Button(frame_input_label, text="📋 Paste", font=("Arial", 8), command=aksi_paste)
    btn_paste.pack(side="right")

    txt_input = tk.Text(root, height=5, width=60)
    txt_input.pack(pady=5)

    # Fungsi untuk tombol utama
    def aksi_enkripsi():
        teks = txt_input.get("1.0", tk.END).strip("\n")
        if not teks:
            messagebox.showwarning("Peringatan", "Teks tidak boleh kosong!")
            return
        hasil = kripto.enkripsi(teks)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, hasil)

    def aksi_dekripsi():
        teks = txt_input.get("1.0", tk.END).strip("\n")
        if not teks:
            messagebox.showwarning("Peringatan", "Teks tidak boleh kosong!")
            return
        hasil = kripto.dekripsi(teks)
        txt_output.delete("1.0", tk.END)
        txt_output.insert(tk.END, hasil)

    def aksi_reset():
        txt_input.delete("1.0", tk.END)
        txt_output.delete("1.0", tk.END)

    # --- FRAME TOMBOL UTAMA ---
    frame_btn = tk.Frame(root)
    frame_btn.pack(pady=10)

    btn_enc = tk.Button(frame_btn, text="Encrypt", width=12, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=aksi_enkripsi)
    btn_enc.grid(row=0, column=0, padx=10)

    btn_dec = tk.Button(frame_btn, text="Decrypt", width=12, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), command=aksi_dekripsi)
    btn_dec.grid(row=0, column=1, padx=10)

    btn_reset = tk.Button(frame_btn, text="Reset", width=12, bg="#f44336", fg="white", font=("Arial", 10, "bold"), command=aksi_reset)
    btn_reset.grid(row=0, column=2, padx=10)

    # --- AREA OUTPUT ---
    frame_output_label = tk.Frame(root)
    frame_output_label.pack(fill="x", pady=(10, 0))

    tk.Label(frame_output_label, text="Hasil:").pack(side="left")
    btn_copy = tk.Button(frame_output_label, text="📑 Copy", font=("Arial", 8), command=aksi_copy)
    btn_copy.pack(side="right")

    txt_output = tk.Text(root, height=5, width=60)
    txt_output.pack(pady=5)

    # --- FOOTER ---
    lbl_footer = tk.Label(root, text="build by.@rhdnxy2026", font=("Arial", 8, "italic"), fg="gray")
    lbl_footer.pack(side="bottom", pady=10)

    # Menjalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    run_gui()