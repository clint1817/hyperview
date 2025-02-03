import os
from cryptography.fernet import Fernet

class HyperView:
    def __init__(self):
        self.key = None
        self.cipher_suite = None
        self.load_or_create_key()

    def load_or_create_key(self):
        """
        Load an existing encryption key or create a new one if it doesn't exist.
        """
        key_file = 'hyperview.key'
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                self.key = file.read()
                print("Encryption key loaded.")
        else:
            self.key = Fernet.generate_key()
            with open(key_file, 'wb') as file:
                file.write(self.key)
                print("New encryption key generated and saved.")
        
        self.cipher_suite = Fernet(self.key)

    def encrypt_file(self, filepath):
        """
        Encrypt the specified file.
        """
        with open(filepath, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = self.cipher_suite.encrypt(file_data)
        
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
        
        print(f"File '{filepath}' encrypted successfully.")

    def decrypt_file(self, filepath):
        """
        Decrypt the specified file.
        """
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        
        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
        
        print(f"File '{filepath}' decrypted successfully.")

    def encrypt_directory(self, directory):
        """
        Encrypt all files in the specified directory.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                self.encrypt_file(filepath)

    def decrypt_directory(self, directory):
        """
        Decrypt all files in the specified directory.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                self.decrypt_file(filepath)

if __name__ == '__main__':
    hv = HyperView()
    # Example usage:
    # hv.encrypt_file('sensitive_data.txt')
    # hv.decrypt_file('sensitive_data.txt')
    # hv.encrypt_directory('sensitive_folder')
    # hv.decrypt_directory('sensitive_folder')