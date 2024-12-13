from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Face Recognition File Security")
    root.geometry("600x400")
    root.configure(bg="#f0f0f5")

    ttk.Style().configure("TButton", font=("Arial", 14), padding=10)

    header = tk.Label(root, text="Face Recognition File Security System", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white")
    header.pack(pady=20, fill="x")

    create_btn = ttk.Button(root, text="Create Secure File", command=create_secure_file)
    open_btn = ttk.Button(root, text="Open Secure File", command=open_secure_file)
    exit_btn = ttk.Button(root, text="Exit", command=root.quit)

    create_btn.pack(pady=10, ipadx=10)
    open_btn.pack(pady=10, ipadx=10)
    exit_btn.pack(pady=10, ipadx=10)

    root.mainloop()

if __name__ == "__main__":
    main()