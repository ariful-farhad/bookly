from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.config import Config
import jwt

password_context = CryptContext(schemes=["bcrypt"])


def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    return hash


def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)


def create_access_token(user_data: dict, expiry: timedelta):

    payload = {}
    token = jwt.encode(
        payload=payload, key=Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM
    )
