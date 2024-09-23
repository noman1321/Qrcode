import qrcode

# Function to generate QR code with a file URL
def generate_qr_code_with_file_url(file_url):
    # Create a QR code with the file URL
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls error correction level
        box_size=10,  # Size of each box
        border=4,  # Thickness of the border
    )
    
    qr.add_data(file_url)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code
    img.save('qr_code_with_file.png')

    print(f'QR Code generated for URL: {file_url}')

# Example file URL (Replace this with your actual file URL)
file_url = 'https://docs.google.com/document/d/1EMgtTHY-MK8JKJUd5EuhJhiirxMhHIur/edit?usp=drive_link&ouid=103026009941191139171&rtpof=true&sd=true'
# Generate the QR code
generate_qr_code_with_file_url(file_url)
