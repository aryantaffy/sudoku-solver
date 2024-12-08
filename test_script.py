from PIL import Image
import pytesseract

# Load the image
image_path = "test_image.jpg"  # Ensure this file is in the same directory as the script
try:
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted Text:")
    print(text)
except FileNotFoundError:
    print(f"Image '{image_path}' not found. Ensure the file is in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
