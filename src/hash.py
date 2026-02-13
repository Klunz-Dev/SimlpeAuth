import os
import hashlib
from typing import Tuple

async def hash_password(password: str) -> Tuple[str, str]:
    try:
        if not password:
            return ValueError('len password < 8')

        salt = os.urandom(16)
        password_bytes = password.encode('utf-8')
        hash_obj = hashlib.sha256()
        hash_obj.update(salt + password_bytes)
        return hash_obj.hexdigest(), salt.hex()
    except Exception as e:
        return e
    
async def verify_password(password: str, save_hash: str, save_salt: str) -> bool:
    try:
        if not password or not save_hash or not save_salt:
            return False
        
        salt = bytes.fromhex()
        password_bytes = password.encode('utf-8')
        hash_obj = hashlib.sha256()
        hash_obj.update(salt + password_bytes)

        return hash_obj.hexdigest() == save_hash

    except Exception as e:
        return e
