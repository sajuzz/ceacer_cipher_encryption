def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift character within alphabet (preserve case)
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Non-alphabet characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Reverse shift character within alphabet (preserve case)
            offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            # Non-alphabet characters remain unchanged
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    # Get user input for message and shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    # Encrypt the message
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Ask if the user wants to decrypt the message
    decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
    
    if decrypt_choice == 'yes':
        # Decrypt the message
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Decryption skipped.")

if __name__ == "__main__":
    main()
