from PIL import Image
import matplotlib.pyplot as plt
import os

# Build the absolute path to the image
image_path = os.path.abspath(os.path.join("..", "image-viz", "images", "example.jpg"))

def display_image(path):
    try:
        # Open the image file
        img = Image.open(path)
        
        # Display the image
        plt.imshow(img)
        plt.axis("off")  # Hide axes
        plt.title("Displaying Image")
        plt.show()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_image(image_path)
