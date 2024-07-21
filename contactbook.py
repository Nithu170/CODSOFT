import tkinter as tk
from tkinter import messagebox

class ContactManagementSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Management System")
        self.window.geometry("600x500")
        self.window.resizable(False, False)

        self.contacts = {}

        self.canvas = tk.Canvas(self.window, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)

        self.create_gradient(self.canvas, 600, 500, "#ff7e5f", "#feb47b")

        self.title_label = tk.Label(self.canvas, text="Contact Management System", font=("Arial", 20, "bold"), bg="#feb47b", fg="#2c3e50")
        self.title_label.pack(pady=20)

        self.form_frame = tk.Frame(self.canvas, bg="#feb47b")
        self.form_frame.pack(pady=10)

        self.create_form_entry("Name:", 0)
        self.create_form_entry("Phone:", 1)
        self.create_form_entry("Email:", 2)
        self.create_form_entry("Address:", 3)

        self.buttons_frame = tk.Frame(self.canvas, bg="#feb47b")
        self.buttons_frame.pack(pady=20)

        self.create_button("Add Contact", self.add_contact, 0)
        self.create_button("View Contacts", self.view_contacts, 1)
        self.create_button("Search Contact", self.search_contact, 2)
        self.create_button("Update Contact", self.update_contact, 3)
        self.create_button("Delete Contact", self.delete_contact, 4)

    def create_gradient(self, canvas, width, height, color1, color2):
        (r1, g1, b1) = self.window.winfo_rgb(color1)
        (r2, g2, b2) = self.window.winfo_rgb(color2)
        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f'#{nr:04x}{ng:04x}{nb:04x}'
            canvas.create_line(0, i, width, i, fill=color)

    def create_form_entry(self, text, row):
        label = tk.Label(self.form_frame, text=text, font=("Arial", 12), bg="#feb47b", fg="#2c3e50")
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(self.form_frame, width=30, font=("Arial", 12))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        setattr(self, text.lower().replace(":", "_entry"), entry)

    def create_button(self, text, command, row):
        button = tk.Button(self.buttons_frame, text=text, command=command, bg="#27ae60", fg="#ecf0f1", font=("Arial", 12, "bold"), activebackground="#2ecc71", activeforeground="#ecf0f1")
        button.grid(row=row, column=0, padx=10, pady=5, sticky="ew")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        contact_list = "\n".join(f"{name}: {details['phone']}" for name, details in self.contacts.items())
        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_term = self.name_entry.get()
        if search_term:
            for name, details in self.contacts.items():
                if search_term in name or search_term in details["phone"]:
                    messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                    return
            messagebox.showerror("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()
