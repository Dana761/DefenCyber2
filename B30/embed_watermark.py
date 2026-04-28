from stegano import lsb

secret_message = "B30_UWA_Perdana_2026"

secret = lsb.hide("original.png", secret_message)
secret.save("watermarked.png")

print("Watermark embedded.")