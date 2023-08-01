import qrcode
import time
print("=== QR Code Generator ===")
print("Github.com/saow")
time.sleep(0.5)
print("This program will generate a QR Code for you.")
print("")
print("")
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)

data = input("Enter the URL to be stored in the QR Code: ")
qr.add_data(data)
qr.make(fit=True)


# Save the QR Code as an image
name = input("Enter name of the file to be saved as: ")
filename = f"{name}.png"
qr.make_image(fill_color="lime", back_color="black").save(filename)
print(f"QR Code saved succefully as {filename}")