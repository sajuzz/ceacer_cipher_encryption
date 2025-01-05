

# Caesar Cipher Encryption and Decryption

This Python project implements the **Caesar Cipher**, a classical encryption algorithm used to shift letters in a message by a specified number. The program allows users to easily encrypt and decrypt messages using a shift value of their choice.

### Features:
- **Encryption**: The program shifts each letter in the input text by a user-defined shift value.
- **Decryption**: Using the same shift value, the program can reverse the encryption and return the original message.
- **Supports Both Uppercase & Lowercase Letters**: The encryption and decryption process preserves the case of the letters.
- **Handles Non-Alphabetic Characters**: Spaces, punctuation marks, and other non-alphabetic characters remain unchanged during both encryption and decryption.
- **Interactive Interface**: Users are prompted to input their message and shift value and can choose to decrypt the encrypted message afterward.

### How It Works:
The Caesar Cipher algorithm is based on shifting each letter of the alphabet by a fixed number of positions. For example:
- If the shift value is `3`, then:
  - 'A' becomes 'D'
  - 'B' becomes 'E'
  - 'C' becomes 'F'
  
The program works by converting each character to its corresponding numeric value using ASCII, applying the shift, and converting it back to a character. For letters, the shift wraps around the alphabet using modulo arithmetic.

### Requirements:
- Python 3.x

### Installation:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd caesar-cipher
   ```
3. Run the program using Python:
   ```bash
   python caesar_cipher.py
   ```

### Usage:
1. **Encrypt a Message**:
   - The program will prompt you to enter a message you want to encrypt.
   - Enter the shift value (an integer, e.g., `3`), which determines how much each letter will be shifted in the alphabet.
   - The program will display the encrypted message.

2. **Decrypt the Message** (Optional):
   - After encrypting, the program will ask if you would like to decrypt the message.
   - If you answer "yes", it will decrypt the message back to its original form using the same shift value.

### Example:

#### Encryption:
```
Enter the message: Hello World!
Enter the shift value (integer): 3
Encrypted message: Khoor Zruog!
```

#### Decryption:
```
Do you want to decrypt the message? (yes/no): yes
Decrypted message: Hello World!
```

### Code Explanation:
- The Caesar Cipher works by shifting each letter by a specified number. This is done by converting characters to their ASCII values, applying the shift, and wrapping around using modulo 26 (since there are 26 letters in the alphabet).
- **Encryption Function**: `caesar_cipher_encrypt` shifts letters forward by the given shift value.
- **Decryption Function**: `caesar_cipher_decrypt` reverses the encryption by shifting letters back by the same shift value.
- **User Interaction**: The program asks for a message, shift value, and whether you want to decrypt the message after encryption.

....

### Conclusion:
The Caesar Cipher is a simple but powerful tool for understanding basic encryption techniques. This program gives users a clear way to experiment with encryption and decryption using customizable shift values. It's a great starting point for learning more about cryptography and encryption algorithms.

