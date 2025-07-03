import hashlib

def hash_text(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()

def hash_file(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        return hashlib.sha512(f.read()).hexdigest()
