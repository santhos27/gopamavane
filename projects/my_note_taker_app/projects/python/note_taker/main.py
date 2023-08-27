import tkinter as tk
from tkinter import messagebox

class NoteTakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taker")

        self.text_area = tk.Text(root, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        save_button = tk.Button(root, text="Save", command=self.save_note)
        save_button.pack(pady=5)

        load_button = tk.Button(root, text="Load", command=self.load_note)
        load_button.pack(pady=5)

    def save_note(self):
        note_content = self.text_area.get("1.0", tk.END)
        try:
            with open("note.txt", "w") as file:
                file.write(note_content)
            messagebox.showinfo("Success", "Note saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def load_note(self):
        try:
            with open("note.txt", "r") as file:
                note_content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", note_content)
        except FileNotFoundError:
            messagebox.showinfo("Info", "No saved note found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakerApp(root)
    root.mainloop()
