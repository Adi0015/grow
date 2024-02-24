from  cryptography.fernet import  Fernet
import  json
import os


class CredentialManager:
    def __init__(self):
        self.filename = os.path.expanduser('~/.config/grow/credentials.json')

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_credentials(self, key, email, password):
        cipher = Fernet(key)
        credentials = f"{email}:{password}"
        return cipher.encrypt(credentials.encode()).decode()

    def decrypt_credentials(self, key, encrypted_credentials):
        cipher = Fernet(key)
        decrypted_credentials = cipher.decrypt(encrypted_credentials.encode()).decode()
        email, password = decrypted_credentials.split(':')
        return email, password

    def save_credentials(self, key, encrypted_credentials):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'w') as f:
            json.dump({"key": key.decode(), "credentials": encrypted_credentials}, f)

    def load_credentials(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data["key"].encode(), data["credentials"]
        except FileNotFoundError:
            return None, None

    def wipe_credentials(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("Credentials wiped successfully.")
        else:
            print("No credentials found.")
