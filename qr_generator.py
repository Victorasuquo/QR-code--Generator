import qrcode


def generate_qrcode(text):
    """
    This function generates a QR code based on the provided text.
    Args:
        text (str): The text to be encoded in the QR code.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("generated.png")

message = input("Enter your text or url to be encoded in the qr code: ")
generate_qrcode(message)
print("your qr code is ready, View it here")


from PIL import Image

# Open the image
image = Image.open("generated.png")

# Display the image
image.show()


