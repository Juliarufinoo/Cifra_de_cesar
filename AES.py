import os
import base64
import time
import pyperclip
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from colorama import Fore, Style, init

init(autoreset=True)

"""

I don't know if you're doing this for class or if you started learning on your own.

So, just in case, let me show you a far more useful and much harder to crack encryption method than the outdated Caesar Cipher.

Don't forget to download "cryptography", "colorama" and "pyperclip", it won't work otherwise.

If you want to reproduce it, by adding/modifying things, this script is really simple. You’ll be able to understand and modify it however you like i guess.

Remember to create ReadMe's that explain your projects. Why, how etc... It's long, it's boring, I know, but you might get the hang of it right away, you'll need it later in your professional life..

Corentin.

"""

# Function to encrypt the text using AES method
def encrypt_aes(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

# Function to encrypt the text using AES method
def decrypt_aes(ciphertext_b64, key):
    ciphertext = base64.b64decode(ciphertext_b64.encode('utf-8'))
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext[16:]) + decryptor.finalize()

# Generate a encryption key
def generate_key():
    return os.urandom(32)

# Check if the input is not empty
def check_input_not_empty(prompt):
    user_input = input(Fore.CYAN + prompt).strip()
    while not user_input:
        print(Fore.RED + "Error: You must enter a value.")
        user_input = input(Fore.CYAN + prompt).strip()
    return user_input

# Display the title
def display_title():
    print(Fore.CYAN + Style.BRIGHT + "\n \n === AES Encryption/Decryption Tool For Julia === \n \n")


def main_menu():
    print(Fore.CYAN + " What would you like to do ? \n")
    print(Fore.CYAN + " 1. Encrypt text")
    print(Fore.CYAN + " 2. Decrypt text")
    print(Fore.CYAN + " 3. Quit \n")
    return input(Fore.YELLOW + "\n Choose an option (1/2/3) : ")


def main():
    display_title()

    while True:
        choice = main_menu()

        if choice == '1':
            data = check_input_not_empty("\n Enter the text to encrypt : ")
            key_choice = input(Fore.YELLOW + "\n Would you like to generate a random key ? (y/n) : ")

            if key_choice.lower() == 'y' or key_choice.strip() == '':
                key = generate_key()
                encoded_key = base64.b64encode(key).decode('utf-8')
                print(Fore.GREEN + "\nGenerated key (keep it safe) : \n \n" + Fore.MAGENTA + encoded_key)
            else:
                try:
                    key = base64.b64decode(check_input_not_empty("\nEnter your key in base64 : ").encode('utf-8'))
                    if len(key) != 32:
                        raise ValueError("The key must be 32 bytes (256 bits).")
                    encoded_key = base64.b64encode(key).decode('utf-8')
                except Exception as e:
                    print(Fore.RED + "\n Error : Invalid key. Please try again.")
                    continue

            ciphertext = encrypt_aes(data, key)
            print(Fore.GREEN + "\nEncrypted text: \n \n" + Fore.MAGENTA + ciphertext)

            clipboard_data = f"Original text : {data} \n Key : {encoded_key} \n Encrypted text : {ciphertext} \n"
            pyperclip.copy(clipboard_data)
            print(Fore.GREEN + "\n Information copied to clipboard ! \n")

        elif choice == '2':
            ciphertext_b64 = check_input_not_empty("\n Enter the encrypted text (base64) : ")
            try:
                key = base64.b64decode(check_input_not_empty("\n Enter your key in base64 : ").encode('utf-8'))
                if len(key) != 32:
                    raise ValueError("The key must be 32 bytes (256 bits).")
                plaintext = decrypt_aes(ciphertext_b64, key)
                print(Fore.GREEN + "Decrypted text: " + Fore.MAGENTA + plaintext.decode('utf-8'))
            except Exception as e:
                print(Fore.RED + f"\n Decryption failed : {str(e)}. Check the key or the encrypted text. \n")

        elif choice == '3':
            print(Fore.RED + "\n Closing script. See you soon ! ")
            time.sleep(2)
            break

        else:
            print(Fore.RED + " Incorrect response, please enter one of the suggested options (1, 2, or 3).")

        # Checkpoint to ask if you want to encrypt, decrypt something else or quit
        retry_choice = input(Fore.YELLOW + " Do you want to return to the main menu or quit ? (m/q) : ")
        if retry_choice.lower() != 'm':
            print(Fore.RED + "\n Closing script. See you soon !")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
