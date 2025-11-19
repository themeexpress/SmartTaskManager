from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv

# Load .env values
load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in .env file")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: str):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"sub": str(subject), "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
