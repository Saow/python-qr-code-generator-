import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr_code():
    data = url_entry.get()
    name = filename_entry.get()
    if data and name:
        try:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
            qr.add_data(data)
            qr.make(fit=True)

            filename = f"{name}.png"
            qr.make_image(fill_color="lime", back_color="black").save(filename)
            messagebox.showinfo("Success", f"QR Code saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter both URL and filename.")

# Create the main window
area = tk.Tk()
area.title("QR Code Generator")
area.geometry("400x210")

# Header label
header_label = tk.Label(area, text="QR Code Generator", font=("Arial", 16))
header_label.pack(pady=10)
header_label2 = tk.Label(area, text="Github.com/saow", font=("Arial", 10))
header_label2.pack(pady=10)

# URL input
url_label = tk.Label(area, text="Enter the URL to be stored in the QR Code:")
url_label.pack()
url_entry = tk.Entry(area, width=40)
url_entry.pack()

# Filename input
filename_label = tk.Label(area, text="Enter name of the file to be saved as: ")
filename_label.pack()
filename_entry = tk.Entry(area, width=40)
filename_entry.pack()

# Generate button
generate_button = tk.Button(area, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Run the main loop
area.mainloop()
