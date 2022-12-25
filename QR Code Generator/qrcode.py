import pyqrcode 
from pyqrcode import QRCode 
  
link = "https://youtu.be/dQw4w9WgXcQ"
  
# Generate QR code 
url = pyqrcode.create(link) 
  
# Create the QR Code
url.svg("QRcode.svg", scale = 8) 