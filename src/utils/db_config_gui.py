import tkinter as tk
from tkinter import messagebox
import pickle
import os

def save_credentials(dbname, user, password, host, port):
    creds = {
        "dbname": dbname,
        "user": user,
        "password": password,
        "host": host,
        "port": int(port)
    }
    os.makedirs("src/data/creds", exist_ok=True)
    with open("src/data/creds/database.pkl", "wb") as file:
        pickle.dump(creds, file)

def on_submit():
    dbname = entry_dbname.get()
    user = entry_user.get()
    password = entry_password.get()
    host = entry_host.get()
    port = entry_port.get()

    if not all([dbname, user, password, host, port]):
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        save_credentials(dbname, user, password, host, port)
        messagebox.showinfo("Success", "Credentials saved to src/data/creds/database.pkl")
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save credentials: {e}")

root = tk.Tk()
root.title("Configure PostgreSQL Database")

tk.Label(root, text="Database Name:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="User:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Password:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Host:").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Port:").grid(row=4, column=0, sticky="e")

entry_dbname = tk.Entry(root, width=30)
entry_user = tk.Entry(root, width=30)
entry_password = tk.Entry(root, show="*", width=30)
entry_host = tk.Entry(root, width=30)
entry_port = tk.Entry(root, width=30)

entry_dbname.grid(row=0, column=1, padx=10, pady=5)
entry_user.grid(row=1, column=1, padx=10, pady=5)
entry_password.grid(row=2, column=1, padx=10, pady=5)
entry_host.grid(row=3, column=1, padx=10, pady=5)
entry_port.grid(row=4, column=1, padx=10, pady=5)

submit_btn = tk.Button(root, text="Save", command=on_submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()