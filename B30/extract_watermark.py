from stegano import lsb

try:
    message = lsb.reveal("modified.png")
    print("Extracted message:", message)
except:
    print("Watermark not detected.")