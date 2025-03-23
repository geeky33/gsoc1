from PIL import Image


# Load the image and store it in a variable
image_path = "data/images/sample.jpg"  # Change to your image path
image_pil = Image.open(image_path)  # Store PIL image for later use

print(image_pil)
