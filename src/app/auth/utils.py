from datetime import datetime, timedelta


import jwt
import bcrypt

from src.config.settings import Settings





def encode_jwt(
        payload: dict,
        private_key: str = Settings.private_key,
        algorithm: str = Settings.algorithm,
        expire_minutes: int = 20
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({'exp' : expire})
    encoded = jwt.encode(to_encode,private_key,algorithm=algorithm)
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = Settings.public_key,
        algorithm: str = Settings.algorithm
):
    decoded = jwt.decode(token,public_key,algorithms=[algorithm])
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_pass: bytes = password.encode()
    return bcrypt.hashpw(pwd_pass,salt)

def validate_password(
        password: str,
        hash_password: bytes
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hash_password
)