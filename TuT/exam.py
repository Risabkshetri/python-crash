from PIL import Image, ImageOps

def pillow_operations():
    image = Image.open("images/example.jpg")

    print("Original Image:")
    image.show()

    # Resize the image
    resized_image = image.resize((200, 200))
    resized_image.show()
    print("Resized the image to 200x200.")

    # Rotate the image
    rotated_image = image.rotate(45)
    rotated_image.show()
    print("Rotated the image by 45 degrees.")

    # Convert to grayscale
    grayscale_image = ImageOps.grayscale(image)
    grayscale_image.show()
    print("Converted the image to grayscale.")

#     # Load an image using OpenCV
#     image = Image.open("images/example.jpg")  # Replace with your image file

#     # Display the original image
#     cv2.imshow("Original Image", image)
#     cv2.waitKey(0)

#     # Convert to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Grayscale Image", gray_image)
#     cv2.waitKey(0)

#     # Resize the image
#     resized_image = cv2.resize(image, (300, 300))
#     cv2.imshow("Resized Image", resized_image)
#     cv2.waitKey(0)

#     # Rotate the image (90 degrees clockwise)
#     rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
#     cv2.imshow("Rotated Image", rotated_image)
#     cv2.waitKey(0)

#     # Apply Gaussian blur
#     blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
#     cv2.imshow("Blurred Image", blurred_image)
#     cv2.waitKey(0)

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Performing operations with Pillow...")
    pillow_operations()
