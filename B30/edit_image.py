from PIL import Image, ImageDraw, ImageEnhance

# Load image
img = Image.open("watermarked.png")

# --- Small safe modification (does NOT destroy watermark) ---
# Slight brightness change
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.02)  # very small change

# Add a small overlay (optional but good for evidence)
draw = ImageDraw.Draw(img)
draw.text((50, 50), "Edited Version", fill=(255, 255, 255))

# Save as PNG (IMPORTANT)
img.save("modified.png")

print("Modified image saved.")