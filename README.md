# PRODIGY_CS_02
Task 2 : Pixel Manipulation for Image Encryption

PROBLEM STATEMENT : Develop a simple image encryption tool using pixel manipulation. 
You can perform operations like swapping pixel values or 
applying a basic mathematical operation to each pixel. 
Allow users to encrypt and decrypt images

VIDEO LINK => https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22app.py%20-%20task2%20-%20Visual%20Studio%20Code%202025-01-10%2000-52-57.mp4%22%2C%22type%22%3A%22video%2Fmp4%22%2C%22signedurl_expire%22%3A%222028-01-09T19%3A52%3A14.346Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F%2F7a9fe192179f4fe1%2Fapp.py%2520-%2520task2%2520-%2520Visual%2520Studio%2520Code%25202025-01-10%252000-52-57.mp4%3FExpires%3D1831060334%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DXetHFe2bWkyxZK96vHWqrLvHv79bwuS6qK6oxMrI8IM~ZC-EL3IRswoaeDodsaKDhb~CzN-APBPHKNdtcahbW~eLixh56cjhhIXjSW4ZH1Bd17iayzeB-6eAcN5RPCxzW78BIKE5lw8ln3TWB5Ts7o93OSbmIXveO0a38H8iEsVrXVL09Ha84DAOTW1tqCsaXaByJifRXPJRrDM6Bitm5SfFCaxJWtygOCCxk9xsD1L5KWib78yExY5XqYM1ly1HARQIjEz2DmHqSEYcw0RpLCNtZWwbknw5yMyA9moVf01DBqtM-zxEOgsXJ6PaboF-3oYiEgasj2-NnLSMf0VthQ__%22%7D

The one with app.py is GUI BASED and one with PMFIE.py is CLI BASED.
Pixel Manipulation for Image Encryption

Problem Statement Overview: The goal is to develop a simple image encryption tool that manipulates the image pixels in a way that makes the image unintelligible, and then allows it to be decrypted back to its original form using a predefined process. The encryption could involve operations like swapping pixel values, applying basic mathematical functions (addition, subtraction, XOR, etc.) to the pixel color channels, or rearranging the pixels themselves.
How the Image Encryption Works:

 Image Representation:
    Images are typically represented as a grid of pixels. Each pixel has color channels like Red, Green, and Blue (RGB). In some cases, images may also include an alpha channel for transparency (RGBA).
        Each pixel has a specific color value that can be represented by an integer value (ranging from 0 to 255 for each channel).

 Encryption Process:
    Swapping Pixel Values: The simplest form of pixel manipulation can involve swapping the color values of pixels. For example, swapping the red and green channels for each pixel in the image.
    Mathematical Operations on Pixel Values: A more advanced form of encryption involves applying a mathematical operation (such as XOR, addition, or subtraction) to each pixel value. This operation can be carried out on each of the color channels (R, G, B) individually or on the entire pixel (all channels together). For example:
    Adding or subtracting a constant to each color value.
    XORing the color values of pixels with a secret key (often referred to as the encryption key).
    Multiplying or dividing the pixel values by a constant factor.
    Pixel Shuffling/Permutation: Instead of just modifying pixel values, another approach involves shuffling the entire set of pixels in the image. You can randomly rearrange the position of pixels within the image matrix to create the encrypted version. The key to this method is knowing the permutation algorithm so that the original image can be reconstructed during decryption.

 Decryption Process:
   Decryption simply reverses the encryption process. If you have swapped pixels or applied mathematical transformations (e.g., addition or XOR), applying the inverse operation restores the original pixel values.
   If the encryption involved swapping pixel color channels, the decryption would involve swapping the channels back to their original positions.
   If the encryption used XOR or addition with a constant, decryption would involve performing the opposite operation (e.g., subtracting the constant or performing XOR with the same key).
   For pixel shuffling, the decryption process involves reversing the pixel permutation using the known encryption key or permutation algorithm.

 Encryption Key:
   The encryption and decryption operations will typically require a key or a seed value that controls how the pixel values are manipulated. For example, when using XOR operations, the key could be a random number or a string that is used to modify the pixel values during encryption and reversed during decryption.
   The key could also control the pixel shuffling process, where the same key is used to "shuffle" and "unshuffle" the pixels in the image.

Example Use Case for the Tool:

Encrypting an Image:
   The user selects an image file (e.g., PNG, JPEG).
   The program asks the user for an encryption key or a shift value, depending on the encryption method.
   The program performs pixel manipulation based on the selected encryption method and key.
   The encrypted image is saved in a new file (e.g., "encrypted_image.jpg").

Decrypting an Image:
  The user selects the encrypted image file.
  The program asks for the same encryption key or shift value used for encryption.
  The program performs the inverse operation on the pixel values, restoring the original image.
  The decrypted image is saved as a new file (e.g., "decrypted_image.jpg").

Encryption Methods Explained:

  Swapping Pixel Channels:
  A simple method where you swap the color channels of the image. For example, swapping the Red and Blue channels for all pixels. This doesn't drastically distort the image but makes it difficult to interpret.

  XOR Encryption:
  XORing each pixel's color values (Red, Green, Blue) with a secret key generates a scrambled image. During decryption, applying the XOR operation with the same key will restore the original image.

  Addition/Subtraction on Pixel Values:
  Adding a fixed value to each of the pixel’s color channels or subtracting a number can obscure the image, making it look entirely different. The same operation (subtracting the value) can then be applied during decryption to recover the original image.

  Pixel Shuffling:
  By changing the positions of the pixels according to a specific pattern or key, the image is encrypted. Decryption reverses the shuffle, placing the pixels back in their original positions.

Security Considerations:

  Key Management: The security of the encryption relies heavily on the key used for encryption. If the key is weak or predictable, the encryption can easily be broken. Thus, it’s important to use a sufficiently random key or password for encryption.
  Complexity of Operations: The more complex the operations (e.g., combining multiple techniques such as XOR with pixel shuffling), the harder it is for attackers to reverse the encryption without knowing the key or algorithm.
