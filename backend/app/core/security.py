from passlib.context import CryptContext

# Configure hashing algorithm (Argon2 is currently recommended by OWASP)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generates a secure hash from a plain password."""
    return pwd_context.hash(password)