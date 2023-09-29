import tkinter as tk
from tkinter import ttk
import pyshorteners
import pyperclip

class URLShortenerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("URL Shortener")
        self.configure(bg="#001524")
        self.geometry("500x400")
        self.iconbitmap(True, 'icon.ico')
        
        self.create_widgets()
        
    def create_widgets(self):
        title_label = ttk.Label(self, text="URL Shortener", foreground="#FFEBEB", font=("Helvetica", 32), background="#001524")
        title_label.pack(pady=10)
        
        long_url_label = ttk.Label(self, text="Enter the link:", foreground="#FFEBEB", background="#001524", font=("Helvetica", 20))
        long_url_label.pack()
        self.long_url_entry = ttk.Entry(self, width=25, font=("Helvetica", 20))
        self.long_url_entry.pack(pady=(0, 10))
        
        style = ttk.Style()
        style.configure("Black.TEntry", foreground="black")
        self.long_url_entry["style"] = "Black.TEntry"
        
        style.configure("TButton", font=("Helvetica", 18))
        
        shorten_button = ttk.Button(self, text="Shorten Link", command=self.shorten_url)
        shorten_button.pack(pady=10)
        
        shortened_url_label = ttk.Label(self, text="Shortened Link:", foreground="#FFEBEB", background="#001524", font=("Helvetica", 20))
        shortened_url_label.pack()
        
        self.shortened_url_entry = ttk.Entry(self, width=25, font=("Helvetica", 20))
        self.shortened_url_entry.pack(pady=(0, 10))
        
        self.shortened_url_entry["style"] = "Black.TEntry"
        
        self.copy_button = ttk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def shorten_url(self):
        long_url = self.long_url_entry.get()
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(long_url)
        self.shortened_url_entry.delete(0, tk.END)
        self.shortened_url_entry.insert(0, shortened_url)
        self.copy_button.config(text="Copy to Clipboard")  
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.shortened_url_entry.get())
        self.copy_button.config(text="Copied!")  

if __name__ == "__main__":
    app = URLShortenerApp()
    app.mainloop()
