import hashlib

class User:

    def __init__(self,username,password,permissions=[]) :
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.permissions = permissions
    
    def __str__(self) -> str:
        return f"Username: {self.username}, Hashed password: {self.password}"