
def encrypt(text, shift):
    encrypted_text = ""
    
    
    for char in text:
        
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    
    
    for char in text:
        
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        
        else:
            decrypted_text += char
    
    return decrypted_text


def is_exact_match(encrypted_input, original_encryption):
    
    return encrypted_input == original_encryption


message = input("Masukkan pesan yang ingin dienkripsi: ")
shift = int(input("Masukkan pergeseran kunci (shift): "))


encrypted_message = encrypt(message, shift)
print("Hasil Enkripsi:", encrypted_message)


while True:
    encrypted_input = input("\nMasukkan pesan yang ingin didekripsi : ")
    
    
    if not is_exact_match(encrypted_input, encrypted_message):
        print("Pesan yang dimasukkan salah. Harap masukkan pesan dengan tepat.")
    else:
        # Jika valid, dekripsi pesan
        decrypted_message = decrypt(encrypted_input, shift)
        print("Hasil Dekripsi:", decrypted_message)
        break
