from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.config import JWTConfig
import jwt
import uuid
import logging

password_context = CryptContext(schemes=['bcrypt'])

def generate_password_hash(password: str) -> str:
    password_hash = password_context.hash(password)

    return password_hash

def verify_password(password: str, password_hash: str) -> bool:
    return password_context.verify(password, password_hash)

def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = {}

    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=JWTConfig.jwt_access_token_expiry))
    payload['jti'] = str(uuid.uuid4())

    payload['refresh'] = refresh

    token = jwt.encode(payload=payload, key=JWTConfig.jwt_secret, algorithm=JWTConfig.jwt_algorithm)

    return token

def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(jwt=token, key=JWTConfig.jwt_secret, algorithms=JWTConfig.jwt_algorithm)

        return token_data

    except jwt.PyJWTError as e:
        logging.exception(e)
        return None

