from flask import Flask, render_template, request, send_from_directory
import os
from PIL import Image
import numpy as np

app = Flask(__name__)

# Paths to save encrypted and decrypted images
ENCRYPTED_FOLDER = 'static/encrypted/'
DECRYPTED_FOLDER = 'static/decrypted/'

# Ensure the folders exist
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Encryption function (XOR-based encryption)
def encrypt_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Define a fixed key for XOR encryption
    key = 42  # Arbitrary integer key for encryption
    
    # Apply XOR operation to encrypt the image
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the result back to an image and save it
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image_path = os.path.join(ENCRYPTED_FOLDER, 'encrypted_image.png')
    encrypted_image.save(encrypted_image_path)
    
    return encrypted_image_path

# Decryption function (reverse of XOR encryption)
def decrypt_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Define the same key used for encryption
    key = 42  # Same key used for encryption
    
    # Apply XOR operation to decrypt the image
    decrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the result back to an image and save it
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image_path = os.path.join(DECRYPTED_FOLDER, 'decrypted_image.png')
    decrypted_image.save(decrypted_image_path)
    
    return decrypted_image_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check for file and get the action (encrypt or decrypt)
        image_file = request.files['image']
        action = request.form.get('action')
        
        # Save the uploaded image
        image_path = os.path.join('static', image_file.filename)
        image_file.save(image_path)
        
        # Process based on action
        if action == 'encrypt':
            encrypted_image_path = encrypt_image(image_path)
            return render_template('index.html', encrypted_image=encrypted_image_path, action="encrypted")
        elif action == 'decrypt':
            decrypted_image_path = decrypt_image(image_path)
            return render_template('index.html', decrypted_image=decrypted_image_path, action="decrypted")
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    # Serve the correct file based on the action
    if 'encrypted' in filename:
        return send_from_directory(ENCRYPTED_FOLDER, filename)
    else:
        return send_from_directory(DECRYPTED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
