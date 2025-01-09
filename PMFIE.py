import os
from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, encryption_key):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to RGB (in case it's in another mode)
    img = img.convert('RGB')

    # Convert image to numpy array
    pixels = np.array(img)
    
    # Apply encryption (a simple addition/subtraction based on the encryption key)
    encrypted_pixels = (pixels + encryption_key) % 256  # Ensure pixel values remain within 0-255 range

    # Convert encrypted pixels back to an image
    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_img.save('encrypted_image.png')  # Save encrypted image
    return encrypted_img

# Function to decrypt the image
def decrypt_image(encrypted_image_path, encryption_key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert encrypted image to numpy array
    encrypted_pixels = np.array(encrypted_img)
    
    # Apply decryption (subtract the encryption key and ensure values stay in the 0-255 range)
    decrypted_pixels = (encrypted_pixels - encryption_key) % 256  # Mod 256 to avoid overflow

    # Convert decrypted pixels back to an image
    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_img.save('decrypted_image.png')  # Save decrypted image
    return decrypted_img

# Function to ask the user for an image file path
def choose_image_file():
    # Prompt the user to enter the path to the image file
    image_path = input("Please enter the path to the image you want to encrypt: ")
    
    # Check if the file exists
    if os.path.isfile(image_path):
        return image_path
    else:
        print("The file does not exist. Please check the path and try again.")
        return None

# Main driver code
def main():
    while True:
        print("Select an option:")
        print("0: Encrypt an image")
        print("1: Decrypt an image")
        print("2: Exit")
        
        choice = input("Enter your choice (0, 1, or 2): ")

        if choice == '0':
            image_path = choose_image_file()
            if image_path:
                encryption_key = int(input("Please enter an encryption key (integer): "))
                encrypted_img = encrypt_image(image_path, encryption_key)
                print("Image encrypted and saved as 'encrypted_image.png'")
            else:
                print("No image selected.")

        elif choice == '1':
            encrypted_image_path = input("Please enter the path to the encrypted image: ")
            decryption_key = int(input("Please enter the decryption key (integer): "))
            decrypted_img = decrypt_image(encrypted_image_path, decryption_key)
            print("Image decrypted and saved as 'decrypted_image.png'")

        elif choice == '2':
            print("Thank you for using this tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the tool
if __name__ == "__main__":
    main()
